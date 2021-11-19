import os
from django.utils import timezone
# from datetime import datetime, timedelta
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard, Visit  # noqa: E402

if __name__ == '__main__':
    # Программируем здесь
    # print('Всего пропусков:', Passcard.objects.count())  # noqa: T001
    # print('Активных пропусков:', Passcard.objects.filter(is_active = True).count())  # noqa: T001
    query = Visit.objects.filter(leaved_at__isnull=True).values()
    print(query)
    
    enter_pers = timezone.localtime(query[0]["entered_at"])
    now = timezone.localtime(timezone.now())
    print(f'Текущее время:\n{now.strftime("%X")}\n')
    delta = now - enter_pers
    seconds = delta.total_seconds()
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds = int(seconds % 60)
    
    for item in query:
      owner = Passcard.objects.filter(id=item["passcard_id"]).values()[0]
      print(owner["owner_name"])
    print(f'Зашёл в хранилище, время по Чите:\n{enter_pers}')
    print('Находится в хранилище:\n{}:{}:{}'.format(hours,minutes,seconds))
    
