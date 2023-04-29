"""
Citește o literă de la tastatură.
    Verifică și afișează dacă este vocală sau nu.

"""
litera = (input("Introduceti o litera: "))
if litera in ("a", "e", "i", "o", "u"):
    print(f" Litera este vocala")
else:
    print(f"Litera este consoana")

# o varianta ar mai fi cu elif si am avea 5 elif pt fiecare vocala in parte