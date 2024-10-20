# MySQL Master-Slave Replication Setup

## Кроки:

1. Створив три контейнери MySQL (mysql-m, mysql-s1, mysql-s2) (docker-compose.yml).
2. Налаштував реплікацію з використанням master-slave.
3. Написав скрипт (write_data.py) для частого запису даних на master-ноду.
4. Переконався, що реплікацію була успішно налаштована.
5. Стопнув один зі слейвів і переконався, що реплікація працює з другим слейвом.
6. Змінити схему на другому слейві, видаливши стовпці:

- остання колонка: успішно, реплікація працює надалі коректно, останнє поле при інсерті скіпається
- колонка в середині таблиці: виникли помилки реплікації, як очікувалося, оскільки майстер передає список усіх
  попередніх полів, включно із видаленим, і репліка не може зматчити коректно поля

## Отже:

Реплікація MySQL чутлива до змін схеми на слейвах. Зміна схеми безпосередньо на слейві може
призвести до помилок реплікації. Необхідно вжити відповідних заходів, щоб переконатися, що зміни схеми застосовані до
мастера та відтворені на слейвах.