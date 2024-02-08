from config import Config 
import requests
from telebot import types
import random
import telebot
from datetime import date ,timedelta ,time
import time 
elhypamody = '6264668799'
bot = telebot.TeleBot(Config.TG_BOT_TOKEN)
p3 = types.InlineKeyboardMarkup()
p5 = types.InlineKeyboardButton(text = "    ",url="t.me/Source_Ze")
A1 = types.InlineKeyboardButton(text = "  .",callback_data="A1")
A2 = types.InlineKeyboardButton(text = "  .",callback_data="A2")
A3 = types.InlineKeyboardButton(text = "  .",callback_data="A3")
A4 = types.InlineKeyboardButton(text = "  ",callback_data="A4")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
  f2 = message.from_user.first_name 
  t2 = message.from_user.username 
  bot.reply_to(message,text="""*   - *[{}](t.me/{})
*     
    *
""".format(f2,t2),disable_web_page_preview=True,parse_mode="markdown")

abod = ["    ",
            "             ",
            "      ",
            "(   )/      ",
            "        ",
            "    ",
            "       ",
            "      ",
            "/   ",
            "   ",
            "            ",
            "    ",
            "     ",
            "    ",
            " |           ",
            "     ",
            "     ",
            "        ",
            "   ",
            "   ",
            "   ",
            "      ",
            "      ",
            "  /    ",
            "     ",
            "    ",
            "      ",
            "   ",
            "      ",
            "      ",
            "  ",
            "        ",
            "     ",
            "   ",
            "     ",
            "      ",
            "     ",
            "      ",
            "   ",
            "       ",
            "       ",
            "   ",
            "       ",
            "    ",
            "   ",
            "   ",
            "   ",
            "    ",
            "   ",
            "  ",
            "      ",
            "     ",
            "     ",
            "       ",
            "   ",
            "  ",
            "      ",
            "          ",
            "     ",
            "       ",
            "   ",
            "      ",
            "    ",
            "     ",
            "    ",
            "    ... ",
            "   ... ",
            "   ",
            "   ",
            "   ",
            " @   ",
            " ",
            "    ",
            "       ",
            "   ",
            " ",
            "   ",
            "  ",
            " @   ",
            "   ",
            "     ",
            "    ",
            "    ",
            "    ",
            "     ",
            "  ",
            "    ",
            "    ",
            "      ",
            "         ",
            "    ",

"  ",
            "      ",
            "     ",
            "      ",
            "  ",
            "   ",
            "            ",
            "     ",
            "   ",
            "  ",
            "   ",
            "      ",
            "  ",
            "    . ",
            "   ",
            "   ",
            "    ",
            "    ",
            "   ",
            "     ",
            "   ",
            "    ",
            "    ",
            "       ",
            "    ",
            "          ",
            "    ",
            "   ",
            "         ",
            "          .",
            "            ",
            "         ",
            "              ",
            "      ",
            "     ",
            "         ",
            "   ",
            "     ",
            "    :      ",
            "          ",
            "  -      ",
            "   ",
            "     ",
            "         ",
            "                 .",
            "          ",
            "      ",
            "     ",
            "   ",
            "       ",
            "   ",
            "         ",
            "      ",
            "    ",
            "  ",
            "     ",
            "      ",
            "     ",
            "     ",
            "     ",
            "       ",
            "           ",
            "    ",
            "     ",
            "  / /     /",
            "      ...",
            "     ",
            "           ",
            "           ",
            "    :   ",
            "          ",
            "      ",
            "         ",
            "    ",
            "     ",
            "    ",
            "         ",
            "     ",
            "            ",
            "              ",

"           ",
            "          ",
            "     ",
            "             ",
            "     ",
            "          ",
            "    ",
            "    ",
            "      ",
            "      ",
            "               ",
            "      ",
            "       ",
            "      ",
            "     ...",
            "     ",
            "     ",
            "     10",
            "           ",
            "      ",
            "             .",
            "           ",
            "      ",
            "         ",
            "    ",
            "           ",
            "    ",
            "     ...",
            "     ",
            "    ",
            "    ",
            "      ",
            "     ",
            "      ",
            "   ",]


n = ["  ",
"   ",
"      ",
"    ",
"   ", 
"     ",
"  ! ",
"   "]
pm = ["  ",
"  ",
" ",
"    ",
"   ",
"",
" ",
" /  ",
"      "]

	
@bot.message_handler(content_types=['text'])
def start(message):
	#if 'http' in message.text:
#		bot.delete_message(id,messagesid)
	if message.text == "" or message.text == "id" or message.text == "":
		n = ["  ",
"   ",
"      ",
"    ",
"   ", 
"     ",
"  ! ",
"   "]
		s333 = random.choice(n)
		url = f"https://t.me/{message.from_user.username}"
		info = bot.get_chat(message.from_user.id)
		bio = info.bio
		c = message.from_user.id
		k = message.from_user.username
		d = time.strftime("%p %H:%M")
		t = message.chat.type
		y = '@Source_Ze'
		bot.send_photo(message.chat.id,url,"""*  {}
		
   {} 

   @{}

    {}

    {} 

   {} *""".format(s333,c,k,d,t,bio),parse_mode="markdown",reply_to_message_id=message.message_id)
	m = message.text
	if m == "":
	 e = message.chat.id
	 u = bot.get_chat(e).photo.big_file.id
	 file_info = bot.get_file(u)
	 downloaded_file = bot
	 download_file(file_info.file_path)
	 with open('new_file.png', 'wb') as new_file:
	 	new_file.write(downloaded_file)
	 	with open('new_file.png', 'rb') as photo:
	 		bot.send_photo(message.chat.id, photo)
	if message.text == "" or message.text == "":
		j = message.chat.title
		t = time.strftime("%p %H:%S")
		l = bot.export_chat_invite_link(message.chat.id)
		f2 = message.from_user.first_name
		t2 = message.from_user.username
		bot.reply_to(message,text="""*
   {} 

   {}

 * [{}](t.me/{}) *

  {}*
""".format(j,l,f2,t2,t),disable_web_page_preview=True,parse_mode="markdown")
	if message.text == " " or message.text == " ":
		if message.reply_to_message:
			f2 = message.reply_to_message.from_user.first_name
			t2 = message.reply_to_message.from_user.username
			bot.reply_to(message,"""*   ** -*  [{}](t.me/{})*
     *""".format(f2,t2),parse_mode="markdown",disable_web_page_preview=True)
	
	m = message.text
	if m == ".":
		f2 = message.from_user.first_name
		p3 = types.InlineKeyboardMarkup()
		p5 = types.InlineKeyboardButton(text = "    ",url="t.me/Source_Ze")
		p3.add(p5)
		bot.reply_to(message,f"{f2}",reply_markup=p3)
	if '@' in message.text.lower():
		bot.delete_message(message.chat.id, message.message_id)
		f2 = message.from_user.first_name
		t2 = message.from_user.username
		bot.send_message(message.chat.id,"""*  * [{}](t.me/{}) 
*   *
""".format(f2,t2),disable_web_page_preview=True,parse_mode="markdown")
	if 'https' in message.text.lower():
		bot.delete_message(message.chat.id, message.message_id)
		f2 = message.from_user.first_name
		t2 = message.from_user.username
		bot.send_message(message.chat.id,"""*  * [{}](t.me/{})
*   *""".format(f2,t2),parse_mode="markdown",disable_web_page_preview=True)
	if message.text == "" or message.text == "" or message.text == "bin":
	  if message.reply_to_message:
	  	bot.pin_chat_messages(message.chat.id,message.reply_to_message.message_id)
	  	bot.reply_to(message,"  !")
	  
	if message.text == " " or message.text == "unban" or message.text == " ":
		if message.reply_to_message:
			bot.unpin_all_chat_message(message.chat.id,message.reply_to_message.message_id)
			bot.reply_to(message,"   !") 
	if m == "" or m == "" or m == "":
		p3 = types.InlineKeyboardMarkup()
		e4 = types.InlineKeyboardButton(text = " .",url="t.me/ZEROR7K7")
		p3.add(e4)
		h = """[  .](t.me/ZEROR7K7)"""
		bot.reply_to(message,h,parse_mode="markdown",reply_markup=p3,disable_web_page_preview=True)
		f2 = message.from_user.first_name
		t2 = message.from_user.username
		l = bot.export_chat_invite_link(message.chat.id)
		y = f"http://t.me/{message.chat.username}/{message.id}"
		o = message.text
		bot.send_message(elhypamody,"""* *: [{}](t.me/{})

*  : {}

  : {}

 : {}*""".format(f2,t2,l,y,o),disable_web_page_preview=True,parse_mode="markdown")
	if m == "":
		f2 = message.from_user.first_name
		f3 = message.from_user.last_name
		bot.reply_to(message,f"""*    {f2}
		
   {f3}*""",parse_mode="markdown")
	if m == "" or m == "":
			t2 = message.from_user.username
			bot.reply_to(message,f"*   @{t2}*",parse_mode="markdown")				
	if m == "" or m == "":
		info = bot.get_chat(message.from_user.id)
		bio = info.bio
		bot.reply_to(message,f"*   {bio}*",parse_mode="markdown")				
	if m == "" or m == "":
		if message.reply_to_message:
			info = bot.get_chat(message.reply_to_message.from_user.id)
			bio = info.bio
			bot.reply_to(message,f"*   {bio}*",parse_mode="markdown")					
	elif message.text == "" or message.text == "":
		if message.reply_to_message:
			f2 = message.reply_to_message.from_user.first_name
			t2 = message.reply_to_message.from_user.username
			c = message.reply_to_message.from_user.id
			k = message.reply_to_message.from_user.username
			d = time.strftime("%p %H:%M")
			
			bot.reply_to(message,text="""*   {} 

   @{}

    {}*""".format(c,t2,d),parse_mode="markdown")		
	if message.text == " " or message.text == " ":
			h222 = ['%90','%80','%70','%60','%50','%40','%30','%20','%10']
			s222 = ["","","","","",""," "," "," "]
			r222 = random.choice(h222)
			d222 = random.choice(s222)
			f2 = message.reply_to_message.from_user.first_name
			t2 = message.reply_to_message.from_user.username
			
			bot.reply_to(message,text="""*  :* [{}](t.me/{})* 
  : {}
  : {}*""".format(f2,t2,r222,d222),disable_web_page_preview=True,parse_mode="markdown")
	if message.text == "" or message.text == "":
	    url = ["https://telegra.ph/file/5047bab5c7a88be186c93.jpg","https://telegra.ph/file/b69cb1ea62b6b63162aca.jpg","https://telegra.ph/file/c621f99ca961ffa2dafb8.jpg","https://telegra.ph/file/5571ba4345056196a6c2b.jpg"]
	    p3 = types.InlineKeyboardMarkup()
	    e3 = types.InlineKeyboardButton(text = "  .",url="t.me/Source_Ze")
	    e4 = types.InlineKeyboardButton(text = " .",url="t.me/ELHYBA")
	    p3.add(e3,e4)
	    r = random.choice(url)
	    h = """     
[  .](t.me/Source_Ze)
[  .](t.me/ELHYBA)"""
	    bot.send_photo(message.chat.id,r,h,reply_to_message_id=message.message_id,reply_markup=p3,parse_mode="markdown")
	if message.text == "e":
		c = bot.get_chat_member_count(chat_id)
		bot.reply_to(message,f"{c}")
	if message.text == "" or message.text == "":
		i = message.from_user.id
		bot.kick_chat_member(message.chat.id,i)
		f2 = message.from_user.first_name
		t2 = message.from_user.username
		bot.reply_to(message,text="*    :* [{}](t.me/{})".format(f2,t2,i),parse_mode="markdown",disable_web_page_preview=True)
	if message.text == "" or message.text == "" or message.text == "":
		if message.reply_to_message.from_user.id:
			bb = message.reply_to_message.from_user.id
			vv = message.reply_to_message.from_user.username
			bot.kick_chat_member(message.chat.id,bb)
			f2 = message.reply_to_message.from_user.first_name
			t2 = message.reply_to_message.from_user.username
			bot.reply_to(message,text="*    :* [{}](t.me/{})".format(f2,t2,vv,bb),parse_mode="markdown",disable_web_page_preview=True)
	if message.text == "" or message.text == "" or message.text == "":
		if message.reply_to_message:
			bb = message.reply_to_message.from_user.id
			vv = message.reply_to_message.from_user.username
			bot.kick_chat_member(message.chat.id,bb)
			f2 = message.reply_to_message.from_user.first_name
			t2 = message.reply_to_message.from_user.username
			bot.reply_to(message,text="*    :* [{}](t.me/{})".format(f2,t2,vv,bb),parse_mode="markdown",disable_web_page_preview=True)
	if message.text == " " or message.text == " ":
		if message.reply_to_message:
			bb = message.reply_to_message.from_user.id
			vv = message.reply_to_message.from_user.username
			bot.unban_chat_member(message.chat.id,bb)
			f2 = message.reply_to_message.from_user.first_name
			t2 = message.reply_to_message.from_user.username
			
			bot.reply_to(message,"""*     :* [{}](t.me/{}) """.format(f2,t2,vv,bb),disable_web_page_preview=True,parse_mode="markdown")
	if message.text == "" or message.text == "":
		p3 = types.InlineKeyboardMarkup()
		p5 = types.InlineKeyboardButton(text = "    ",url="t.me/Source_Ze")
		A1 = types.InlineKeyboardButton(text = "  .",callback_data="A1")
		A2 = types.InlineKeyboardButton(text = "  .",callback_data="A2")
		A3 = types.InlineKeyboardButton(text = "  .",callback_data="A3")
		A4 = types.InlineKeyboardButton(text = "  ",callback_data="A4")
		p3.add(A1,A2)
		p3.add(A3,A4)
		p3.add(p5)
		f2 = message.from_user.first_name 
		t2 = message.from_user.username
		bot.reply_to(message,text="""*   - *[{}](t.me/{})
*     
  *
""".format(f2,t2),disable_web_page_preview=True,parse_mode="markdown",reply_markup=p3)
	p3 = types.InlineKeyboardMarkup()
	p5 = types.InlineKeyboardButton( "    ",url="t.me/Source_Ze")
	p3.add(p5)
	if message.text == "" or message.text == " " or message.text == " ":
		photo_str =  random.randint(74,154)
		avtar_ainme = "https://t.me/PhotosDavid/" + str(photo_str)
		bot.send_photo(message.chat.id,avtar_ainme,"""*    
- - - -- - - - - -- - - - -
CH - @Source_Ze*""",parse_mode="markdown",reply_to_message_id=message.message_id,reply_markup=p3)
	p3 = types.InlineKeyboardMarkup()
	p5 = types.InlineKeyboardButton( "    ",url="t.me/Source_Ze")
	p3.add(p5)
	
	
	if "" in message.text:
	 m = message
	 mm = message.text
	 k = "    "
	 rep=str(message.text).split(" ")
	 bot.reply_to(m,mm.replace("","    "))	
	if message.text == "" or message.text == "" or message.text == " " or message.text == " ":
		photo_str =  random.randint(74,154)
		avtar_ball = "https://t.me/avtar781/" + str(photo_str)
		bot.send_photo(message.chat.id,avtar_ball,"""*    
- - - -- - - - - -- - - - -
CH - @Source_Ze*""",parse_mode="markdown",reply_to_message_id=message.message_id,reply_markup=p3)
	if message.text == "" or message.text == "" or message.text == "":
		song_str = random.randint(74,154)
		song_voice = "https://t.me/vVvdav/" + str(song_str)
		bot.send_audio(message.chat.id,song_voice,"""*     
- @Sss0s0bot*""",parse_mode="markdown",reply_to_message_id=message.message_id,reply_markup=p3)
	if message.text == "" or message.text == "":
		song_str = random.randint(74,904)
		song_voice = "https://t.me//" + str(song_str)
		bot.send_voice(message.chat.id,song_voice,"""*     
- @Sss0s0bot*""",parse_mode="markdown",reply_to_message_id=message.message_id,reply_markup=p3)
	if message.text == "" or message.text == "":
		song_str = random.randint(74,154)
		song_voice = "https://t.me/DjAseel/" + str(song_str)
		bot.send_audio(message.chat.id,song_voice,"""*     
- @Sss0s0bot*""",parse_mode="markdown",reply_to_message_id=message.message_id,reply_markup=p3)
	if message.text == "":
		bot.reply_to(message,"  ")
	elif message.text == "":
		bot.reply_to(message,"   ")
	elif message.text=="":
		bot.reply_to(message,".")
	elif message.text==" ":
			bot.reply_to(message,".  ")
	elif message.text=="":
			bot.reply_to(message,".  ")
	elif message.text=="":
			bot.reply_to(message,"  ")
	elif message.text=="":
			bot.reply_to(message,"   ")
	elif message.text=="":
			bot.reply_to(message,"   ")
	elif message.text=="":
			bot.reply_to(message,"   ")
	elif message.text=="":
		bot.reply_to(message,"  ")
	elif message.text==" ":
		bot.reply_to(message,"   !!.")
	elif message.text=="":
		bot.reply_to(message,"    ")
		
	elif "" in message.text or "" in message.text or ""in message.text:
		bot.reply_to(message,"  ")#  

	elif message.text ==" ":
		bot.reply_to(message,"    ")
	elif message.text=="":
		bot.reply_to(message,"")
	elif message.text=="":
		bot.reply_to(message,".")
	elif message.text=="":
		bot.reply_to(message,".")
	elif message.text =="":
	  bot.reply_to(message,"  .")
	elif message.text =="":
	  bot.reply_to(message,"     ")
	 
	elif message.text =="" :
		bot.reply_to(message,"    ")

	  
	
	m = message.text	
	if m == "" or m == "" or m == "" or m == "":
		p3 = types.InlineKeyboardMarkup()
		p5 = types.InlineKeyboardButton(text = "    ",url="t.me/Source_Ze")
		
		p3.add(p5)
		t = time.strftime("%p%H:%S")
		t = time.strftime("%Y/%m/%d %A %b")
		bot.reply_to(message,f" {t}",reply_markup=p3)
	
			
	m = message.text
	if m == "" or m == "" or m == "":
		p3 = types.InlineKeyboardMarkup()
		p5 = types.InlineKeyboardButton(text = "    ",url="t.me/Source_Ze")
		p3.add(p5)
		t = time.strftime("%p %H:%S")
		bot.reply_to(message,f" {t}",reply_markup=p3)	
	m = message.text
	if m == "" or m == "" or m == "":
		url = f"https://t.me/{message.from_user.username}"
		bot.send_photo(message.chat.id,url,reply_to_message_id=message.message_id)
	if "" in message.text:
	 m = message.text
	 k = "   "
	 rep=str(message.text).split("")
	 bot.reply_to(message,k+m)	
	m = message.text		
	if m == "" or m == "" :
		l = bot.export_chat_invite_link(message.chat.id)
		bot.reply_to(message,f"""*   : 
{l}*""",parse_mode="markdown")
	     	
	if message.text == "" or message.text == "" or message.text == "" or message.text == "" or message.text == "":
	  p3 = types.InlineKeyboardMarkup()
	  p5 = types.InlineKeyboardButton(text = "    ",url="t.me/Source_Ze")
	  url = "https://ApiAzkar.amoapi.repl.co"
	  msg = message.text
	  p3.add(p5)
	  t = requests.get(url).text
	  j = """      
     ============================"""
	  bot.reply_to(message,f"*{j}\n{t}*",parse_mode="markdown",reply_markup=p3)

	if message.text == '' or message.text == ' ' or message.text == "":

	    	p3 = types.InlineKeyboardMarkup()
	    	p5 = types.InlineKeyboardButton(text = "    ",url="t.me/Source_Ze")
	    	p4 = types.InlineKeyboardButton(text ='', callback_data= 'c2')
	    	r = random.choice(abod)
	    	p3.add(p4)
	    	p3.add(p5)
	    	bot.reply_to(message,f"""*{r}
- - - - - - - - - - - - - 
@Tuupacbot*""",parse_mode="markdown",reply_markup=p3)
@bot.callback_query_handler(func= lambda call : True)
def callback_data(call):
  
  if call.data == "c2":
  	r = random.choice(abod)
  	p3 = types.InlineKeyboardMarkup()
  	p5 = types.InlineKeyboardButton(text = "    ",url="t.me/Source_Ze")
  	p4 = types.InlineKeyboardButton(text ='', callback_data= 'c2')
  	p3.add(p4)
  	p3.add(p5)
  	bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f"""*{r}
- - - - - - - - - - - - - -
@Tuupacbot*""",reply_markup=p3,parse_mode="markdown")
  p3 = types.InlineKeyboardMarkup()
  s0 = types.InlineKeyboardButton(text = "",callback_data="s0")
  A1 = types.InlineKeyboardButton(text = "  .",callback_data="A1")
  A2 = types.InlineKeyboardButton(text = "  .",callback_data="A2")
  A3 = types.InlineKeyboardButton(text = "  .",callback_data="A3")
  A4 = types.InlineKeyboardButton(text = "  ",callback_data="A4")
  p3.add(A1,A2)
  p3.add(A3,A4)
  if call.data == "s0":
  	f2 = call.from_user.first_name
  	t2 = call.from_user.username
  	bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="""*   - *[{}](t.me/{})
*     
  *
""".format(f2,t2),disable_web_page_preview=True,parse_mode="markdown",reply_markup=p3)
  
  if call.data == "A1":
      p3 = types.InlineKeyboardMarkup()
      s0 = types.InlineKeyboardButton(text = "",callback_data="s0")
      p3.add(s0)
      bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="""* 
  - - - - - - - - - - - - - 
  <<
   << 
  <<
   <<
  <<
  <<
   <<
  <<
  <<
  <<
  <<
  <<
   <<
  <<
  <<*""",parse_mode="markdown",reply_markup=p3)
  
#####+#####
u = 70
a = 1
uu = u - a 
print(f"f > m  = {uu}")
bot.polling()
