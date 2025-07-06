import csv
from urllib.parse import quote

# ✅ Full list of Riyadh districts
riyadh_districts = [
    'الصحافة', 'النرجس', 'الياسمين', 'العارض', 'القيروان', 'الربيع', 'الندى', 'الغدير',
    'الملقا', 'المرسلات', 'المروج', 'الازدهار', 'الفلاح', 'العقيق', 'السمحان', 'حطين', 'النخيل',
    'الربوة', 'الورود', 'الرحمانية', 'الرائد', 'الوادي', 'السامرية', 'الشفا', 'الدار البيضاء',
    'العزيزية', 'المنصورة', 'منفوحة', 'منفوحة الجديدة', 'السلام', 'النسيم الشرقي', 'النسيم الغربي',
    'الفيحاء', 'المنار', 'الروابي', 'النهضة', 'الريان', 'النظيم', 'الخليج', 'الرمال', 'المنتزه',
    'السعادة', 'الربية', 'ظهرة البديعة', 'العريجاء الوسطى', 'العريجاء الغربية', 'السويدي الغربي',
    'طويق', 'الغروب', 'العليا', 'الملز', 'الروضة الشمالية', 'السليمانية', 'المعذر الشمالي',
    'أم الحمام الشرقي', 'أم الحمام الغربي', 'المربع', 'الفوطة', 'الوزارات', 'السلي', 'الجزيرة',
    'الندوة', 'الجنادرية', 'المعيزيلة', 'الحمراء', 'أشبيلية', 'اليرموك', 'القادسية', 'قرطبة',
    'غرناطة', 'البيان', 'اليرموك الشرقي', 'المونسية', 'الشرق', 'الرابية', 'الزاهري'
]

# ✅ File name
csv_filename = "barbershop_links.csv"

# ✅ Step 1: Read already existing districts from the CSV
done_districts = set()
try:
    with open(csv_filename, mode='r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        for row in reader:
            done_districts.add(row["الحي"])
except FileNotFoundError:
    pass  # If file not found, assume no districts done yet

# ✅ Step 2: Identify remaining districts
remaining_districts = [d for d in riyadh_districts if d not in done_districts]

# ✅ Step 3: Append remaining links
with open(csv_filename, mode='a', newline='', encoding='utf-8-sig') as file:
    writer = csv.writer(file)
    if not done_districts:
        writer.writerow(["الحي", "Google Maps Link"])  # Header if file was empty
    for district in remaining_districts:
        query = f"صالون حلاقة رجال {district} الرياض"
        url = f"https://www.google.com/maps/search/{quote(query)}"
        writer.writerow([district, url])

print(f"✅ Added {len(remaining_districts)} new district links to {csv_filename}")
