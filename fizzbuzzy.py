from collections import Counter
import discord
from discord.ext import commands

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def is_fibonacci(n):
    a, b = 0, 1
    while a < n:
        a, b = b, a + b
    return a == n

def is_square_free(n):
    for i in range(2, int(n**0.5) + 1):
        if n % (i**2) == 0:
            return False
    return True

def is_sum_of_squares(n):
    for i in range(1, int(n**0.5) + 1):
        j = n - i**2
        if (j**0.5).is_integer():
            return True
    return False

def is_a_power(n):
    idx = 15
    array = [[i**j for j in range(idx)] for i in range(idx)]

    for i in range(idx):
        for j in range(idx):
            if (array[i][j] == n):
                return True
                break

    return False

def prime_factors(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2

    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n = n // i

    if n > 2:
        factors.append(n)

    factor_counter = Counter(factors)
    factor_counter_dict = dict(factor_counter)

    total = 0
    for value in factor_counter_dict.values():
        total += value

    if total == 3:
        return True
    return False

def multiple_prime_factors(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2

    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n = n // i

    if n > 2:
        factors.append(n)

    factor_counter = Counter(factors)
    factor_counter_dict = dict(factor_counter)

    if len(factor_counter_dict.keys()) >= 2:
        return True
    return False

def fizzbuzz_extended(n):
    output = ''

    if n % 5 == 0 or '5' in str(n):
        output += 'bang '
    if n % 7 == 0 or '7' in str(n):
        output += 'buzz '
    if is_prime(n):
        output += 'crash '
    if is_fibonacci(n):
        output += 'fibbi '
    if is_sum_of_squares(n):
        output += 'squawk '
    if is_square_free(n):
        output += 'whizz '
    if multiple_prime_factors(n):
        output += 'pop '
    if is_a_power(n):
        output += 'zip '
    if prime_factors(n):
        output += 'triple '

    if not output:
        output = str(n)

    return output.strip()

def check_answers(user_answer_list, answer_list):
    for answer in user_answer_list:
        if answer in answer_list:
            answer_list.remove(answer)
        elif answer not in answer_list:
            return False
            break

    if len(answer_list) > 0:
        return False

    return True

def run():
    intents = discord.Intents.default()
    intents.message_content = True
    intents.messages = True
    intents.members = True
    intents.guilds = True
    bot = commands.Bot(command_prefix='~', intents=intents)
    current_number = 1

    @bot.event
    async def on_ready():
        print(bot.user)
        print(bot.user.id)
        print('---------------')

    @bot.command()
    async def ping(ctx):
        await ctx.send('pong')

    @bot.command()
    async def rules(ctx):
        await ctx.send('rules for fizzbuzz: https://media.discordapp.net/attachments/1167631521193152523/1170593298793119834/IMG_9764.jpg?width=556&height=741')
        await ctx.send('to play the game, type whatever buzz words apply to the number in chat (order doesnt matter). if ur right, the bot will continue; if ur wrong, the game will reset. you win once you hit 999. SPELLING MATTERS')

    @bot.command()
    async def fizzbuzz(ctx):
        if ctx.channel.name != 'quib':
            await ctx.send("This game is only allowed in the 'quib' channel.")
            return

        await ctx.send('Starting a new fizzbuzz round')

        for i in range(1, 1000):
            await ctx.send(f'current number: {i}')
            answer = fizzbuzz_extended(i)
            answer_list = answer.split(' ')
            print(answer)

            def check_message(message):
                return message.channel.name == 'quib' and message.author != bot.user

            user_answer = await bot.wait_for('message', check=check_message)
            user_answer_list = user_answer.content.split(' ')
            print(user_answer_list)

            if check_answers(user_answer_list, answer_list):
                    await ctx.send('correct')
            else:
                await ctx.send(
                    'incorrect answer. if you would like to play again, run the fizzbuzz command once more.')
                break

    bot.run('tokem')

if __name__ == '__main__':
    run()
