from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import (
    api_view, authentication_classes, permission_classes,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from main.models import Experience, Volunteering
from main.permissions import IsPortfolioOwnerOrEditorOrReadOnly
from main.serializers import ExperienceSerializer, VolunteeringSerializer


@api_view(["GET", "HEAD", "POST"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsPortfolioOwnerOrEditorOrReadOnly])
def experience_list(request):
    if request.method in ("GET", "HEAD"):
        experiences = Experience.objects.prefetch_related("starred_by").order_by("title", "id")
        title = request.query_params.get("title", "").strip()
        if title:
            experiences = experiences.filter(title__icontains=title)
        serializer = ExperienceSerializer(
            experiences, many=True, context={"request": request},
        )
        return Response(serializer.data)

    serializer = ExperienceSerializer(data=request.data, context={"request": request})
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["GET", "HEAD", "PUT", "PATCH", "DELETE"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsPortfolioOwnerOrEditorOrReadOnly])
def experience_detail(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method in ("GET", "HEAD"):
        serializer = ExperienceSerializer(
            experience, context={"request": request}
        )
        return Response(serializer.data)

    if request.method == "DELETE":
        experience.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    serializer = ExperienceSerializer(
        experience,
        data=request.data,
        partial=request.method == "PATCH",
        context={"request": request},
    )
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)

@api_view(["POST"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def experience_star(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)

    if experience.starred_by.filter(pk=request.user.pk).exists():
        experience.starred_by.remove(request.user)
    else:
        experience.starred_by.add(request.user)

    serializer = ExperienceSerializer(
        experience, context={"request": request}
    )
    return Response(serializer.data)


@api_view(['GET', 'POST'])
@authentication_classes([SessionAuthentication])
@permission_classes([IsPortfolioOwnerOrEditorOrReadOnly])
def volunteering_list(request):
    if request.method == 'GET':
        volunteerings = Volunteering.objects.all()

        search_query = request.GET.get('search', '')
        if search_query:
            volunteerings = volunteerings.filter(
                title__icontains=search_query
            )

        serializer = VolunteeringSerializer(
            volunteerings,
            many=True,
            context={'request': request}
        )
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = VolunteeringSerializer(
            data=request.data,
            context={'request': request}
        )

        if serializer.is_valid():
            volunteering = serializer.save()
            return Response(
                VolunteeringSerializer(
                    volunteering,
                    context={'request': request}
                ).data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
@authentication_classes([SessionAuthentication])
@permission_classes([IsPortfolioOwnerOrEditorOrReadOnly])
def volunteering_detail(request, id):
    try:
        volunteering = Volunteering.objects.get(pk=id)
    except Volunteering.DoesNotExist:
        return Response(
            {'detail': 'Not found.'},
            status=status.HTTP_404_NOT_FOUND
        )

    if request.method == 'GET':
        serializer = VolunteeringSerializer(
            volunteering,
            context={'request': request}
        )
        return Response(serializer.data)

    elif request.method in ['PUT', 'PATCH']:
        serializer = VolunteeringSerializer(
            volunteering,
            data=request.data,
            partial=(request.method == 'PATCH'),
            context={'request': request}
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    elif request.method == 'DELETE':
        volunteering.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def volunteering_star(request, id):
    try:
        volunteering = Volunteering.objects.get(pk=id)
    except Volunteering.DoesNotExist:
        return Response(
            {'detail': 'Not found.'},
            status=status.HTTP_404_NOT_FOUND
        )

    if volunteering.starred_by.filter(id=request.user.id).exists():
        volunteering.starred_by.remove(request.user)
        starred = False
    else:
        volunteering.starred_by.add(request.user)
        starred = True

    return Response({
        'starred': starred,
        'star_count': volunteering.starred_by.count()
    })
