from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from habits.models import Habits
from habits.paginations import HabitsPagination
from habits.serializers.habits import HabitsSerializer
from users.permissions import IsOwner

# from habits.tasks import send_message_about_habits_time


class HabitCreateAPIView(CreateAPIView):
    """Класс создания привычки"""
    serializer_class = HabitsSerializer
    queryset = Habits.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_habit = serializer.save()
        new_habit.owner = self.request.user
        new_habit.save()


class HabitListAPIView(ListAPIView):
    """Класс получения списка привычек, доступных текущему пользователю"""
    serializer_class = HabitsSerializer
    queryset = Habits.objects.all()
    pagination_class = HabitsPagination
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        user = self.request.user
        habits_list = super().get_queryset()
        return habits_list.filter(owner=user)


class HabitDetailAPIView(RetrieveAPIView):
    """Класс получения подробностей о привычке"""
    serializer_class = HabitsSerializer
    queryset = Habits.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class HabitUpdateAPIView(UpdateAPIView):
    """Класс обновления привычки"""
    serializer_class = HabitsSerializer
    queryset = Habits.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class HabitDeleteAPIView(DestroyAPIView):
    """Класс удаления привычки"""
    serializer_class = HabitsSerializer
    queryset = Habits.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class HabitPublicListAPIView(ListAPIView):
    """Класс получения списка публичных привычек, доступных всем пользователям"""
    serializer_class = HabitsSerializer
    queryset = Habits.objects.all().filter(is_public=True)
    pagination_class = HabitsPagination
    permission_classes = [IsAuthenticated]
