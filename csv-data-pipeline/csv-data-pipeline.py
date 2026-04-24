import csv

valid = []
city = {}

total = 0
skipped = 0
adults = 0
minors = 0

with open("day-02 input.csv") as f:
    reader = csv.DictReader(f)

    for row in reader:
        total += 1

        if not row["name"].strip() or not row["age"].strip() or not row["city"].strip():
            skipped += 1
            continue

        try:
            age = int(row["age"].strip())
        except ValueError:
            print(f"error at {row}")
            skipped += 1
            continue

        city_name = row["city"].strip()

        if age >= 18:
            adults += 1

            valid.append({
                "name": row["name"].strip(),
                "age": age,
                "city": city_name
            })

            city[city_name] = city.get(city_name, 0) + 1

        else:
            minors += 1

print(f"Adults: {adults}")
print(f"Minors: {minors}")
print(f"Skipped: {skipped}")

top_city = max(city, key=city.get)
print(f"Top city: {top_city} ({city[top_city]} adults)")

with open("valid.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "age", "city"])
    writer.writeheader()
    writer.writerows(valid)
with open("city-count.csv","w",newline='')as f:
    writer = csv.DictWriter(f, fieldnames=["city","count"])
    writer.writeheader()
    for key,value in city.items():
        writer.writerow({"city":key,"count":value})