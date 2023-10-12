import nextcord
from nextcord.ext import commands, tasks

intents = nextcord.Intents.all()

bot = commands.Bot(command_prefix="/", intents=intents)

check_online_task = None 

@bot.event
async def on_ready():
    print("""
        ██╗        ██╗      ██╗██╗     ███████╗
        ██║        ██║   ██║██║     ╚════██║
        ██║        ██║      ██║██║       ███╔═╝
        ██║     ██║      ██║██║     ██╔══╝
        ███████╗╚██████╔╝███████╗███████╗
        ╚══════╝ ╚═════╝ ╚══════╝╚══════╝
    """)
    check_online.start()

@bot.slash_command(
    name="start_check",
    description="Check if user is online"
)
async def start_check(ctx):
    global check_online_task  # Global olarak tanımlanan görevi kontrol etmek için

    if not check_online_task or check_online_task.done():  # Görev başlatılmadıysa veya tamamlandıysa
        check_online_task = check_online.start()
        await ctx.send("Started unroler")
    else:
        await ctx.send("Unroler is already running.")

@bot.slash_command(
    name="stop_check",
    description="Stop checking"
)
async def stop_check(ctx):
    global check_online_task 

    if check_online_task and not check_online_task.done(): 
        check_online_task.cancel()
        await ctx.send("Stopped unroler.")
    else:
        await ctx.send("Unroler is not running.")

@tasks.loop(seconds=5)
async def check_online():
    user_ids = [1152288539019587727, 1152241539892916254]
    role_names = ["nigger", "• Santa 🎄", "Bots"] 
    for user_id in user_ids:
        user = await bot.fetch_user(user_id)
        member = nextcord.utils.get(bot.get_all_members(), id=user.id)
        if member:
            if member.status == nextcord.Status.online:
                for role_name in role_names:
                    role = nextcord.utils.get(member.guild.roles, name=role_name)
                    if role:
                        await member.add_roles(role)
                print(f"{member.name} is online.")
            else:
                for role_name in role_names:
                    role = nextcord.utils.get(member.guild.roles, name=role_name)
                    if role:
                        await member.remove_roles(role)
                print(f"{user.name} is offline")

bot.run("MTE1NDQzMDQxMDE2NDU1MTgwMQ.GXnfop.t1_JknAcbT8NXHrEcRAVh3s1opYtBcFObYmCpk")
