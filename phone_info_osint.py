# phone_info_osint.py
# Simple public phone info OSINT tool (for learning only)

import phonenumbers
from phonenumbers import carrier, geocoder, timezone

print("📱 Phone Number OSINT Tool (Public Info Only)\n")

# User input
number = input("👉 Enter phone number (with country code): ")

try:
    phone = phonenumbers.parse(number)
    print("\n✅ Number parsed successfully!\n")

    # Basic info
    print("🌍 Region:", geocoder.description_for_number(phone, "en"))
    print("⏰ Timezone:", timezone.time_zones_for_number(phone))
    print("📶 Carrier:", carrier.name_for_number(phone, "en"))
    print("🆔 Valid:", phonenumbers.is_valid_number(phone))
    print("📞 Possible:", phonenumbers.is_possible_number(phone))

except Exception as e:
    print("\n❌ Error:", e)
