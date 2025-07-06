from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import csv
import os

# CSV path (you can change this to an absolute path if needed)
csv_file = "riyadh_barbershop_template.csv"

# List of Riyadh districts
riyadh_districts = [
    "الصحافة", "النرجس", "الياسمين", "العارض", "القيروان", "الربيع", "الندى", "الغدير", "الملقا",
    "المرسلات", "المروج", "الازدهار", "الفلاح", "العقيق", "السمحان", "حطين", "النخيل", "الربوة",
    "الورود", "الرحمانية", "الرائد", "الوادي"
]

# Setup Chrome options
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_experimental_option("detach", True)

# Start Chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Write header only once
if not os.path.exists(csv_file):
    with open(csv_file, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        writer.writerow(["اسم الصالون", "الحي", "العنوان", "رقم الجوال", "رابط الإنستغرام", "رابط الواتساب", "ملاحظات"])

# Start scraping
for district in riyadh_districts:
    query = f"صالون حلاقة رجال {district} الرياض"
    print(f"🔍 Searching: {query}")
    driver.get("https://www.google.com/maps")
    time.sleep(3)

    try:
        # Search the query
        search_box = driver.find_element(By.ID, "searchboxinput")
        search_box.clear()
        search_box.send_keys(query)
        driver.find_element(By.ID, "searchbox-searchbutton").click()
        time.sleep(6)

        # Get list of barber shops in results
        results = driver.find_elements(By.CSS_SELECTOR, 'a.hfpxzc')[:5]

        print(f"📍 Found {len(results)} listings in {district}")

        for i, result in enumerate(results, 1):
            try:
                result.click()
                time.sleep(4)

                # Extract data from the side panel
                name = driver.find_element(By.CSS_SELECTOR, 'h1.DUwDvf').text
                try:
                    address = driver.find_element(By.CSS_SELECTOR, 'div[data-item-id="address"]').text
                except:
                    address = "غير متوفر"

                try:
                    phone = driver.find_element(By.CSS_SELECTOR, 'div[data-tooltip="نسخ رقم الهاتف"]').text
                except:
                    phone = "غير متوفر"

                # Instagram and WhatsApp: requires deep scraping (not easily available)
                insta = "غير متوفر"
                whatsapp = "غير متوفر"

                with open(csv_file, "a", newline="", encoding="utf-8-sig") as f:
                    writer = csv.writer(f)
                    writer.writerow([name, district, address, phone, insta, whatsapp, ""])
                print(f"✅ Saved: {name}, {address}, {phone}")

            except Exception as e:
                print(f"❌ Error in result {i} for {district}: {str(e)}")

    except Exception as e:
        print(f"❌ Search error for {district}: {str(e)}")

# Done
driver.quit()
print(f"\n🎉 All done. Data saved to: {csv_file}")
