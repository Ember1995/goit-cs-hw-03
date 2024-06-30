from pymongo import MongoClient
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId

# Підключення до MongoDB
client = MongoClient(
    "mongodb+srv://hannadunska:<hidden_for_security_reason>@cluster0.gpl8kd8.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
    server_api=ServerApi('1')
)

# Створення бази даних "book"
db = client.book

# Створення колекції "cats"
collection = db.cats

def create_cat(name, age, features):
    """
    Створює нового кота у колекції.

    Args:
        name (str): Ім'я кота.
        age (int): Вік кота.
        features (list): Список характеристик кота.
    """
    cat = {
        "name": name,
        "age": age,
        "features": features
    }
    result = collection.insert_one(cat)
    print(f"Inserted cat with id: {result.inserted_id}")

def read_all_cats():
    """
    Виводить всі записи з колекції.
    """
    cats = collection.find({})
    for cat in cats:
        print(cat)

def read_cat_by_name(name):
    """
    Виводить інформацію про кота за ім'ям.

    Args:
        name (str): Ім'я кота.
    """
    cat = collection.find_one({"name": name})
    if cat:
        print(cat)
    else:
        print("Cat not found")

def update_cat_age(name, new_age):
    """
    Оновлює вік кота за ім'ям.

    Args:
        name (str): Ім'я кота.
        new_age (int): Новий вік кота.
    """
    result = collection.update_one({"name": name}, {"$set": {"age": new_age}})
    if result.modified_count > 0:
        print(f"Updated age of {name}")
    else:
        print(f"No cat found with name {name}")

def add_feature_to_cat(name, feature):
    """
    Додає нову характеристику до списку features кота за ім'ям.

    Args:
        name (str): Ім'я кота.
        feature (str): Нова характеристика.
    """
    result = collection.update_one({"name": name}, {"$push": {"features": feature}})
    if result.modified_count > 0:
        print(f"Added feature to {name}")
    else:
        print(f"No cat found with name {name}")

def delete_cat_by_name(name):
    """
    Видаляє запис з колекції за ім'ям тварини.

    Args:
        name (str): Ім'я кота.
    """
    result = collection.delete_one({"name": name})
    if result.deleted_count > 0:
        print(f"Deleted cat with name {name}")
    else:
        print(f"No cat found with name {name}")

def delete_all_cats():
    """
    Видаляє всі записи з колекції.
    """
    result = collection.delete_many({})
    print(f"Deleted {result.deleted_count} cats")

if __name__ == "__main__":
    try:
        # Створення нових котів
        create_cat("barsik", 3, ["ходить в капці", "дає себе гладити", "рудий"])
        create_cat("Lama", 2, ["ходить в лоток", "не дає себе гладити", "сірий"])
        create_cat("Liza", 4, ["ходить в лоток", "дає себе гладити", "білий"])

        # Читання всіх котів
        print("All cats:")
        read_all_cats()

        # Читання кота за ім'ям
        print("Read cat by name:")
        read_cat_by_name("barsik")

        # Оновлення віку кота
        print("Update cat age:")
        update_cat_age("barsik", 4)

        # Додавання нової характеристики коту
        print("Add feature to cat:")
        add_feature_to_cat("barsik", "полюбляє спати")

        # Видалення кота за ім'ям
        print("Delete cat by name:")
        delete_cat_by_name("barsik")

        # Видалення всіх котів
        print("Delete all cats:")
        delete_all_cats()

    except Exception as e:
        print(f"An error occurred: {e}")
