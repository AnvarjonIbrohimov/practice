** NestJS ozi nima?  **
    NestJS bu EXPRESS ni ustida qurilgan framework hisoblanadi
    🔹 1. NestJS — bu Node.js yordamida server (backend) yaratish uchun framework.
      ⚡ Efficient → tez va samarali ishlaydi
      📈 Progressive → oddiydan boshlab, katta projectga oson o‘tasiz
      🔒 Reliable → ishonchli va barqaror
      📦 Scalable → yuklamarni kattalashtirish kengaytirish oson
    🔹 2. TypeScript bilan ishlaydi   
      Toliq typeScriptda ishlab juda xam katta loyihani NestJS ishlash oson

    🔹 3. Bir nechta programming usullarni birlashtiradi
      🧠 OOP → class va object bilan ishlash
      🔁 AOP → (AOP — Aspect-Oriented Programming) 
          logging, auth kabi umumiy narsalarni alohida boshqarish
      ⚙️ Functional programming → funksiyalar orqali yozish

    🔹 4. Muhim pattern (tuzilmalar) ishlatadi
      🏗 MVC → Controller orqali request boshqarish
      🔌 DI (Dependency Injection) → class ichiga kerakli narsani avtomatik berish
      🔄 Middleware → request kelganda oldin ishlaydigan kod
      🎯 Decorator → @Get(), @Controller() kabi maxsus belgilar

    🔹 5. NestJS CLI (tool) Command Line Interface
        👉 Terminal orqali boshqarish
            Komanda yozib ishlaysiz (nest new, npm start)

** NestJS ingridient nima **
    *CONTROLLER*
      👉 Requestni qabul qiladi (entry point)
        * Frontend → backendga request yuboradi
        * Controller uni qabul qiladi va servicega beradi

    *MODULES*
      👉 Hammasini birlashtiradi
        Controller + Service ni ulaydi
        Har bir feature uchun alohida module bo‘ladi

    *SERVICES*
      👉 Business logic shu yerda yoziladi
        Ma’lumotni qayta ishlaydi
        Database bilan ishlaydi

    *GUARDS*
      👉 Ruxsat tekshiradi (auth)
        Kim kirishi mumkinligini aniqlaydi
        Login qilinganmi yo‘qmi tekshiradi

    *PIPES*
      👉 Data’ni tekshiradi va o‘zgartiradi
        Validation qiladi
        Formatni to‘g‘rilaydi

** NestJS Module decorator **
  @Module({  👉 Module — bu konteyner (yig‘uvchi)
  controllers: [UserController],  👉 Qaysi controllerlar shu modulga tegishli
  providers: [UserService],    👉 Service va boshqa logiclar shu yerda bo‘ladi
  imports: [AuthModule],      👉 Boshqa modullarni ulash
  exports: [UserService],      👉 Shu moduldagi service’ni boshqa modullarga berish
})


** NestJS da Rest API va Zoo  ** 

nest -v => qaysi versiyada ekanini korsatadi
nest --help  => commant line da qanday mantiqlar borligini korsatadi 
nest g --help => 
** VS Code terminalda **
    nest g module cat      =>  module file generat qilib beradi
    nest g controller cat      =>  bu cat uchun avtomat controller ochib uni file lar bilan boglab beradi
    nest g service cat      =>  bu xam cat uchun avtomat service ochib uni file lar bilan boglab beradi