Client → Resolver → Guard → Pipe → Service → Interceptor → Response

🚀 NESTJS GRAPHQL INGREDIENTS (INGREDIENTS = tarkibiy qismlari)
**********************************************************************
🧠 1. RESOLVER Nima qiladi?
➡️ GraphQL’da kelgan query va mutation larni ushlab, javob qaytaradi
Oddiy qilib:
👉 Frontend savol beradi → Resolver javob beradi
**********************************************************************
📦 2. MODULES Nima qiladi?
➡️ Barcha qismlarni (resolver, service) bir joyga yig‘adi
Oddiy qilib:
👉 Bu — loyiha ichidagi “papka / container”
**********************************************************************
⚙️ 3. SERVICES Nima qiladi?
➡️ Asosiy biznes logika shu yerda yoziladi
Oddiy qilib:
👉 “Real ish shu yerda bajariladi”
(masalan: database bilan ishlash)
**********************************************************************
🔐 4. GUARDS Nima qiladi?
➡️ Kim kirishi mumkinligini tekshiradi
Oddiy qilib:
👉 Login qilganmi? Role bormi? — tekshiradi
**********************************************************************
🔄 5. PIPES Nima qiladi?
➡️ Kelgan ma’lumotni tekshiradi va o‘zgartiradi 
Oddiy qilib:
👉 Input to‘g‘rimi? Format to‘g‘rimi? — validate qiladi
**********************************************************************
🎯 6. INTERCEPTOR Nima qiladi?
➡️ Request/response dan oldin yoki keyin ishlaydi
Oddiy qilib:
👉 Log yozish, vaqt o‘lchash, response o‘zgartirish
🔥 QISQA FLOW (eng muhim!)
**********************************************************************
