*****************************************************************************************
# 🔹 1. Standard mode nima?
  👉 Bu oddiy loyiha (single app)

# 🔥 2. Monorepo mode nima?
  👉 Bu bir nechta app + shared code bitta project ichida
*****************************************************************************************
                    GraphQL API   ==> kearkli data
👉 Client (frontend) o‘zi kerakli datani tanlab oladi

                        ___________
              HTTP      |         | ----->      Auth APIs   👉 Login / register / token berish
GraphQL API ------- =>  |GraphQL  | ----->      Core APIs   👉 Loyihaning asosiy API lari
                        |         | ----->      Redis       👉 Juda tez ishlaydigan database (memoryda ishlaydi)
                        -----------
**************************************************************************
                    REST API     ==> tayyor data  
👉 Oldindan belgilangan endpointlar orqali ishlaydi

              HTTP      REST API   |----->      Auth APIs   👉 Login / register / token berish
Rest API    ------- =>  REST API   |----->      Core APIs   👉 Loyihaning asosiy API lari
                        REST API   |----->      Redis       👉 Juda tez ishlaydigan database (memoryda ishlaydi)

*****************************************************************************************
1. driver: ApolloDriver 
  GraphQL serverni qaysi engine bilan ishlatishni belgilaydi
    👉 Apollo Server
    👉 Oddiy qilib: “GraphQL backendni kim boshqaradi?” → Apollo

2. playground: true
  Browserda GraphQL test qilish uchun UI ochadi
  URL: http://localhost:3000/graphql
  👉 Agar false qilsangiz → UI yopiladi

3. uploads: false
  File upload funksiyasini o‘chiradi
  👉 false bo‘lsa:
    GraphQL orqali file yuklab bo‘lmaydi
  👉 true qilinsa:
    rasm, file yuborish mumkin (lekin qo‘shimcha sozlash kerak)

4. autoSchemaFile: true
  GraphQL schema (type definitions) ni avtomatik yaratadi
  👉 NestJS o‘zi:
    @ObjectType()
    @Field()
    @Resolver()
      lardan schema (.gql) fayl yasaydi


*****************************************************************************************

Apollo — bu GraphQL bilan ishlash uchun tool (platforma)
  👉 Asosan 2 qismdan iborat:
    1. Apollo Server:
      Backend uchun GraphQL API yaratadi
    2. Apollo Client:
      Frontend uchun (React, Vue va h.k.) GraphQL API ga so‘rov yuboradi


*****************************************************************************************
    
📥 1. QUERY       -> ➡️ Ma’lumotni olish (GET)
      👉 bu: userlar ro‘yxatini olib keladi
✏️ 2. MUTATION    -> ➡️ Ma’lumotni o‘zgartirish (POST / PUT / DELETE)
      👉 bu: yangi user yaratadi
🔄 3. SUBSCRIPTION  -> ➡️ Real-time update
      👉 yangi user qo‘shilsa → avtomatik keladi
🧠 4. RESOLVER    ->  ➡️ Yuqoridagi query/mutation/subscriptionni bajaradigan funksiya
      👉 “Backend ichidagi ishlovchi miyasi”
      
*****************************************************************************************
📦 1. DTO (Data Transfer Object)  ➡️ Backendga keladigan data strukturasi (shape)
      👉 Vazifasi:
                  requestni tartibga soladi va validation qiladi
🔄 2. INTERCEPTOR  ➡️ Request va Response orasida ishlaydigan layer
      👉 Vazifasi: 
                  log yozish response o‘zgartirish  vaqt o‘lchash

*****************************************************************************************
📦 MODULE:  ➡️ Featurelarni guruhlaydi
  👉 Vazifasi:
              Resolver, Service, Controllerlarni birlashtiradi
              👉 Module = “container / papka”

🧱 MODEL: ➡️ Database strukturasi
    👉 Vazifasi:
                DB dagi jadval yoki schema
                👉 Model = “database jadvali”

                Client → DTO → Resolver → Service → Model → Database
                ↓
           Interceptor
*****************************************************************************************