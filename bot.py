import os

import discord
from dotenv import load_dotenv
from discord.ext import commands
from discord.ui import View, Button

# ==========================================================
# LOAD ENVIRONMENT
# ==========================================================

load_dotenv()

TOKEN = os.getenv("TOKEN")

if not TOKEN:
    raise ValueError(
        "TOKEN tidak ditemukan!\n"
        "Pastikan file .env berada pada folder yang sama dengan bot.py"
    )

# ==========================================================
# YOBLOX CONFIG
# ==========================================================

BOT_NAME = "YOBLOX"
BOT_PREFIX = "!"

EMBED_COLOR = discord.Color.blurple()

EMBED_FOOTER = "YOBLOX • Community"

# ==========================================================
# CHANNEL CONFIG
# ==========================================================

# Channel Panel Citizen
SELF_ROLE_CHANNEL = 1470498490818756877

# Channel Panel Game
GAME_ROLE_CHANNEL = 1470498490818756877

# ==========================================================
# ROLE CONFIG
# ==========================================================

CITIZEN_ROLE = 1438554888845000784

# ==========================================================
# GAME ROLE CONFIG
# ==========================================================

ROBLOX_ROLE = 1529083414869839973
VALORANT_ROLE = 1529083451670794351
MOBILE_LEGENDS_ROLE = 1529083498340552796

# ==========================================================
# CUSTOM EMOJI
# ==========================================================

ROBLOX_EMOJI = discord.PartialEmoji(
    name="roblox",
    id=1529086818367311873
)

VALORANT_EMOJI = discord.PartialEmoji(
    name="valorant",
    id=1529086677006680064
)

MOBILE_LEGENDS_EMOJI = discord.PartialEmoji(
    name="mobilelegends",
    id=1529086764797661314
)

# ==========================================================
# GIF BANNER
# ==========================================================

GIF_URL = (
    "https://cdn.discordapp.com/attachments/1470498490818756877/1490736800090689687/standard_2.gif?ex=6a4dc595&is=6a4c7415&hm=8640860778d9a819e9e7908acbb88db0250227196fc1d482f6294dda0f3bd89c&"
)

# ==========================================================
# BOT INTENTS
# ==========================================================

intents = discord.Intents.default()
intents.guilds = True
intents.members = True
intents.message_content = True
intents.presences = True

# ==========================================================
# CREATE BOT
# ==========================================================

bot = commands.Bot(
    command_prefix=BOT_PREFIX,
    intents=intents,
    help_command=None
)

# ==========================================================
# CONSTANT
# ==========================================================

SUCCESS_COLOR = discord.Color.green()
ERROR_COLOR = discord.Color.red()
REMOVE_COLOR = discord.Color.orange()

BUTTON_LABEL = "Citizen"
BUTTON_EMOJI = "🔰"
BUTTON_STYLE = discord.ButtonStyle.success
BUTTON_CUSTOM_ID = "yoblox_citizen"

# ==========================================================
# EMBED DESCRIPTION
# ==========================================================

SELFROLE_DESCRIPTION = (
    "## 📌 INFORMATION\n\n"

    "👋 Selamat datang di **YOBLOX Community!**\n"

    "🔰 Ambil role **Citizen** untuk mendapatkan akses penuh ke seluruh server.\n"

    "🌐 Jelajahi berbagai channel, ikuti event komunitas, dan temui member baru.\n"

    "✨ Kami senang kamu menjadi bagian dari **YOBLOX**.\n\n"

    "━━━━━━━━━━━━━━━━━━━━━━\n\n"

    "## 🔰 CITIZEN ROLE\n\n"

    "Tekan tombol **Citizen** di bawah untuk mendapatkan "
    "atau menghapus role kapan saja."
)

# ==========================================================
# GAME ROLE DESCRIPTION
# ==========================================================

GAMEROLE_DESCRIPTION = (
    "Pilih game favoritmu untuk mendapatkan akses "
    "ke channel dan informasi sesuai game yang kamu mainkan.\n\n"

    "━━━━━━━━━━━━━━━━━━━━━━\n\n"

    f"{ROBLOX_EMOJI} **Roblox**\n"
    f"{VALORANT_EMOJI} **Valorant**\n"
    f"{MOBILE_LEGENDS_EMOJI} **Mobile Legends**\n\n"

    "━━━━━━━━━━━━━━━━━━━━━━\n\n"

    "Tekan tombol di bawah untuk mengambil "
    "atau menghapus role kapan saja."
)
# ==========================================================
# CITIZEN ROLE VIEW
# ==========================================================

class CitizenRoleView(View):

    def __init__(self):
        super().__init__(timeout=None)

        citizen_button = Button(
            label=BUTTON_LABEL,
            emoji=BUTTON_EMOJI,
            style=BUTTON_STYLE,
            custom_id=BUTTON_CUSTOM_ID
        )

        citizen_button.callback = self.citizen_callback

        self.add_item(citizen_button)

    async def citizen_callback(
        self,
        interaction: discord.Interaction
    ):

        member = interaction.guild.get_member(
            interaction.user.id
        )

        role = interaction.guild.get_role(
            CITIZEN_ROLE
        )

        # ==========================================
        # VALIDATION
        # ==========================================

        if member is None:

            return await interaction.response.send_message(
                "❌ Member tidak ditemukan.",
                ephemeral=True
            )

        if role is None:

            return await interaction.response.send_message(
                "❌ Role Citizen tidak ditemukan.",
                ephemeral=True
            )

        me = interaction.guild.me

        if role >= me.top_role:

            return await interaction.response.send_message(
                (
                    "❌ Role Citizen berada di atas role bot.\n\n"
                    "Pindahkan role bot ke atas Role Citizen."
                ),
                ephemeral=True
            )

        # ==========================================
        # REMOVE ROLE
        # ==========================================

        if role in member.roles:

            try:

                await member.remove_roles(
                    role,
                    reason="YOBLOX Self Role"
                )

                embed = discord.Embed(
                    title="🔰 Citizen Role",
                    description=(
                        f"Role {role.mention} berhasil dihapus.\n\n"
                        "Kamu dapat mengambil role kembali kapan saja."
                    ),
                    color=REMOVE_COLOR
                )

                embed.set_footer(
                    text=EMBED_FOOTER
                )

                return await interaction.response.send_message(
                    embed=embed,
                    ephemeral=True
                )

            except discord.Forbidden:

                return await interaction.response.send_message(
                    (
                        "❌ Bot tidak memiliki izin "
                        "**Manage Roles**."
                    ),
                    ephemeral=True
                )

        # ==========================================
        # ADD ROLE
        # ==========================================

        try:

            await member.add_roles(
                role,
                reason="YOBLOX Self Role"
            )

            embed = discord.Embed(
                title="🎉 Selamat Datang!",
                description=(
                    f"Role {role.mention} berhasil ditambahkan.\n\n"
                    "Selamat datang di **YOBLOX Community!**\n\n"
                    "Semoga betah dan selamat menikmati komunitas kami. 🚀"
                ),
                color=SUCCESS_COLOR
            )

            if interaction.guild.icon:

                embed.set_thumbnail(
                    url=interaction.guild.icon.url
                )

            embed.set_footer(
                text=EMBED_FOOTER
            )

            await interaction.response.send_message(
                embed=embed,
                ephemeral=True
            )

        except discord.Forbidden:

            await interaction.response.send_message(
                (
                    "❌ Bot tidak memiliki permission "
                    "**Manage Roles**."
                ),
                ephemeral=True
            )

        except Exception as e:

            await interaction.response.send_message(
                f"❌ Terjadi kesalahan.\n```{e}```",
                ephemeral=True
            )
# ==========================================================
# GAME ROLE VIEW
# ==========================================================

class GameRoleView(View):

    def __init__(self):
        super().__init__(timeout=None)

        self.add_item(
            Button(
                label="Roblox",
                emoji=ROBLOX_EMOJI,
                style=discord.ButtonStyle.secondary,
                custom_id="game_roblox"
            )
        )

        self.add_item(
            Button(
                label="Valorant",
                emoji=VALORANT_EMOJI,
                style=discord.ButtonStyle.secondary,
                custom_id="game_valorant"
            )
        )

        self.add_item(
            Button(
                label="Mobile Legends",
                emoji=MOBILE_LEGENDS_EMOJI,
                style=discord.ButtonStyle.secondary,
                custom_id="game_mobile_legends"
            )
        )

        self.children[0].callback = self.roblox_callback
        self.children[1].callback = self.valorant_callback
        self.children[2].callback = self.mobile_legends_callback

    # ======================================================
    # UNIVERSAL TOGGLE ROLE
    # ======================================================

    async def toggle_role(
        self,
        interaction: discord.Interaction,
        role_id: int,
        role_name: str
    ):

        member = interaction.guild.get_member(interaction.user.id)

        if member is None:
            return await interaction.response.send_message(
                "❌ Member tidak ditemukan.",
                ephemeral=True
            )

        role = interaction.guild.get_role(role_id)

        if role is None:
            return await interaction.response.send_message(
                f"❌ Role {role_name} tidak ditemukan.",
                ephemeral=True
            )

        me = interaction.guild.me

        if role >= me.top_role:
            return await interaction.response.send_message(
                "❌ Role berada di atas role bot.",
                ephemeral=True
            )

        # ==========================================
        # REMOVE ROLE
        # ==========================================

        if role in member.roles:

            try:

                await member.remove_roles(
                    role,
                    reason="YOBLOX Game Role"
                )

                embed = discord.Embed(
                    title="🎮 Game Role",
                    description=(
                        f"Role {role.mention} berhasil dihapus."
                    ),
                    color=REMOVE_COLOR
                )

                embed.set_footer(text=EMBED_FOOTER)

                return await interaction.response.send_message(
                    embed=embed,
                    ephemeral=True
                )

            except discord.Forbidden:

                return await interaction.response.send_message(
                    "❌ Bot tidak memiliki permission **Manage Roles**.",
                    ephemeral=True
                )

        # ==========================================
        # ADD ROLE
        # ==========================================

        try:

            await member.add_roles(
                role,
                reason="YOBLOX Game Role"
            )

            embed = discord.Embed(
                title="✅ Role Ditambahkan",
                description=(
                    f"Role {role.mention} berhasil ditambahkan.\n\n"
                    f"Selamat bermain **{role_name}**! 🎉"
                ),
                color=SUCCESS_COLOR
            )

            if interaction.guild.icon:
                embed.set_thumbnail(
                    url=interaction.guild.icon.url
                )

            embed.set_footer(
                text=EMBED_FOOTER
            )

            await interaction.response.send_message(
                embed=embed,
                ephemeral=True
            )

        except discord.Forbidden:

            await interaction.response.send_message(
                "❌ Bot tidak memiliki permission **Manage Roles**.",
                ephemeral=True
            )

        except Exception as e:

            await interaction.response.send_message(
                f"❌ Terjadi kesalahan.\n```{e}```",
                ephemeral=True
            )

    # ======================================================
    # CALLBACK
    # ======================================================

    async def roblox_callback(
        self,
        interaction: discord.Interaction
    ):
        await self.toggle_role(
            interaction,
            ROBLOX_ROLE,
            "Roblox"
        )

    async def valorant_callback(
        self,
        interaction: discord.Interaction
    ):
        await self.toggle_role(
            interaction,
            VALORANT_ROLE,
            "Valorant"
        )

    async def mobile_legends_callback(
        self,
        interaction: discord.Interaction
    ):
        await self.toggle_role(
            interaction,
            MOBILE_LEGENDS_ROLE,
            "Mobile Legends"
        )
# ==========================================================
# BOT READY
# ==========================================================

@bot.event
async def on_ready():

    # Persistent Button
    bot.add_view(CitizenRoleView())
    bot.add_view(GameRoleView())

    print("=" * 60)
    print("✅ BOT BERHASIL ONLINE")
    print("=" * 60)
    print(f"🤖 Bot Name : {bot.user}")
    print(f"🆔 Bot ID   : {bot.user.id}")
    print(f"📚 Guild    : {len(bot.guilds)}")
    print("=" * 60)

    activity = discord.Activity(
        type=discord.ActivityType.watching,
        name="YOBLOX Community 🔰"
    )

    await bot.change_presence(
        status=discord.Status.online,
        activity=activity
    )

    print("✅ Citizen Role Loaded")
    print("✅ Game Role Loaded")
    print("🚀 YOBLOX Ready!")


# ==========================================================
# COMMAND : PING
# ==========================================================

@bot.command(
    name="ping",
    help="Melihat latency bot."
)
async def ping(ctx):

    latency = round(bot.latency * 1000)

    embed = discord.Embed(
        title="🏓 Pong!",
        description=(
            f"**Latency:** `{latency} ms`\n\n"
            "Bot berjalan dengan normal."
        ),
        color=EMBED_COLOR
    )

    embed.set_footer(text=EMBED_FOOTER)

    await ctx.send(embed=embed)
# ==========================================================
# COMMAND : SELF ROLE PANEL
# ==========================================================

@bot.command(
    name="selfrole",
    help="Mengirim panel Self Role."
)
@commands.has_permissions(administrator=True)
async def selfrole(ctx):

    channel = bot.get_channel(SELF_ROLE_CHANNEL)

    if channel is None:
        return await ctx.send(
            "❌ Channel Self Role tidak ditemukan."
        )

    try:
        await ctx.message.delete()
    except discord.Forbidden:
        pass

    embed = discord.Embed(
        title="🎭 YOBLOX",
        description=SELFROLE_DESCRIPTION,
        color=EMBED_COLOR
    )

    if GIF_URL:
        embed.set_image(url=GIF_URL)

    if ctx.guild.icon:
        embed.set_thumbnail(
            url=ctx.guild.icon.url
        )

    embed.set_footer(text=EMBED_FOOTER)

    await channel.send(
        embed=embed,
        view=CitizenRoleView()
    )

    success = discord.Embed(
        description="✅ Panel Citizen Role berhasil dikirim.",
        color=SUCCESS_COLOR
    )

    await ctx.send(
        embed=success,
        delete_after=5
    )


# ==========================================================
# COMMAND : GAME ROLE PANEL
# ==========================================================

@bot.command(
    name="gamerole",
    help="Mengirim panel Game Role."
)
@commands.has_permissions(administrator=True)
async def gamerole(ctx):

    channel = bot.get_channel(GAME_ROLE_CHANNEL)

    if channel is None:
        return await ctx.send(
            "❌ Channel Game Role tidak ditemukan."
        )

    try:
        await ctx.message.delete()
    except discord.Forbidden:
        pass

    embed = discord.Embed(
        title="🎮 Game Role",
        description=GAMEROLE_DESCRIPTION,
        color=EMBED_COLOR
    )

    if GIF_URL:
        embed.set_image(url=GIF_URL)

    if ctx.guild.icon:
        embed.set_thumbnail(
            url=ctx.guild.icon.url
        )

    embed.set_footer(text=EMBED_FOOTER)

    await channel.send(
        embed=embed,
        view=GameRoleView()
    )

    success = discord.Embed(
        description="✅ Panel Game Role berhasil dikirim.",
        color=SUCCESS_COLOR
    )

    await ctx.send(
        embed=success,
        delete_after=5
    )
# ==========================================================
# COMMAND ERROR
# ==========================================================

async def send_permission_error(ctx):

    embed = discord.Embed(
        title="❌ Permission Ditolak",
        description=(
            "Kamu harus memiliki permission "
            "**Administrator** untuk menggunakan command ini."
        ),
        color=ERROR_COLOR
    )

    await ctx.send(
        embed=embed,
        delete_after=5
    )


@selfrole.error
async def selfrole_error(ctx, error):

    if isinstance(error, commands.MissingPermissions):
        return await send_permission_error(ctx)

    raise error


@gamerole.error
async def gamerole_error(ctx, error):

    if isinstance(error, commands.MissingPermissions):
        return await send_permission_error(ctx)

    raise error


# ==========================================================
# RUN BOT
# ==========================================================

if __name__ == "__main__":

    try:

        print("=" * 60)
        print(f"🚀 Menjalankan {BOT_NAME}")
        print("=" * 60)

        bot.run(TOKEN)

    except discord.LoginFailure:

        print("\n❌ TOKEN BOT INVALID")
        print("Silakan periksa kembali TOKEN pada file .env")

    except KeyboardInterrupt:

        print("\n🛑 Bot dihentikan oleh pengguna.")

    except Exception as e:

        print("\n❌ Terjadi kesalahan saat menjalankan bot:")
        print(e)