from aiogram import Router, F
from aiogram.types import Message, chat_member_updated, CallbackQuery
from aiogram.types.chat_member import ChatMember
from aiogram.filters import CommandStart, Command
from keyboards.inline import start_menu
from loader import bot
from aiogram.fsm.context import FSMContext
from states.royxat import Form

start_router: Router = Router()

@start_router.message(CommandStart())
async def start_handler(message:Message):
    await message.answer(f"""Assalom alaykum{message.from_user.full_name} \nUstoz shogird kanalining rasmiy botiga xush kelibsiz!
    \n/help yordam buyrugi orqali nimalarga qodir ekanligimni bilib oling!
     """, reply_markup=start_menu)
    
@start_router.message(F.text == "Sherik kerak")
async def menu(message:Message, state: FSMContext):
    await message.answer(f"""Sherik topish uchun ariza berish
 \nHozir sizga birnecha savollar beriladi. \nHar biriga javob bering. \nOxirida agar hammasi to'g'ri bo'lsa, ha tugmasini bosing va arizangiz Adminga yuboriladi.                    
""")
    await state.set_state(Form.ism)
    await message.answer("Ism, familiyangizni kiritng")
    
@start_router.message(Form.ism)
async def get_name(message:Message, state:FSMContext):
    await state.update_data(ism=message.text)
    await state.set_state(Form.texnolog)

    await message.answer(f"""📚 Texnologiya:
\nTalab qilinadigan texnologiyalarni kiriting? \nTexnologiya nomlarini vergul bilan ajrating. Masalan, 
\nJava, C++, C#
""")
    
@start_router.message(Form.texnolog)
async def get_texno(message:Message, state: FSMContext):
    await state.update_data(texnolog = message.text)
    await state.set_state(Form.aloqa)
    await message.answer("""📞 Aloqa: 
\nBog`lanish uchun raqamingizni kiriting? \nMasalan, +998 90 123 45 67                    
""")
    
@start_router.message(Form.aloqa)
async def get_aloqa(message:Message, state: FSMContext):
    await state.update_data(aloqa = message.text)
    await state.set_state(Form.hudud)
    await message.answer("""🌐 Hudud:  
\nQaysi hududdansiz? \nViloyat nomi, Toshkent shahar yoki Respublikani kiriting.                  
""")
    
@start_router.message(Form.hudud)
async def get_hudud(message:Message, state: FSMContext):
    await state.update_data(narxi = message.text)
    await state.set_state(Form.narxi)
    await message.answer("""💰 Narxi: 
\nTolov qilasizmi yoki Tekinmi? \nKerak bo`lsa, Summani kiriting?                 
""")
    
@start_router.message(Form.narxi)
async def get_hudud(message:Message, state: FSMContext):
    await state.update_data(hudud = message.text)
    await state.set_state(Form.kasbi)
    await message.answer("""👨🏻‍💻 Kasbi: 
\nIshlaysizmi yoki o`qiysizmi? \nMasalan, Talaba               
""")
    
@start_router.message(Form.kasbi)
async def get_hudud(message:Message, state: FSMContext):
    await state.update_data(kasbi = message.text)
    await state.set_state(Form.vaqt)
    await message.answer("""🕰 Murojaat qilish vaqti: 
\nQaysi vaqtda murojaat qilish mumkin? \nMasalan, 9:00 - 18:00              
""")
    
@start_router.message(Form.vaqt)
async def get_hudud(message:Message, state: FSMContext):
    await state.update_data(vaqt = message.text)
    await state.set_state(Form.maqsad)
    await message.answer("""🔎 Maqsad: 
\nMaqsadingizni qisqacha yozib bering.            
""")
    
@start_router.message(Form.maqsad)
async def get_maqsad(message:Message, state: FSMContext):
    await state.update_data(maqsad=message.text)
    malumot = await state.get_data()
    await state.clear()
    await message.answer(f"""Sherik kerak:
🏅 Sherik: {malumot['ism']} \n📚 Texnologiya: {malumot['texnolog']} \n🇺🇿 Telegram: @{message.from_user.username} \n📞 Aloqa: {malumot['aloqa']} \n🌐 Hudud: {malumot['hudud']} \n💰 Narxi: {malumot['narxi']} \n👨🏻‍💻 Kasbi: {malumot['kasbi']} \n 🕰 Murojaat qilish vaqti: {malumot['vaqt']} \n 🔎 Maqsad: {malumot['maqsad']}
""")
    
    


