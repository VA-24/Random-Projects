from collections import Counter
import discord
from discord.ext import commands
import json
import random
import asyncio

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
    powers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 9, 27, 81, 243, 729, 2187, 6561, 19683, 59049, 177147, 531441, 1594323, 4782969, 16, 64, 256, 1024, 4096, 16384, 65536, 262144, 1048576, 4194304, 16777216, 67108864, 268435456, 25, 125, 625, 3125, 15625, 78125, 390625, 1953125, 9765625, 48828125, 244140625, 1220703125, 6103515625, 36, 216, 1296, 7776, 46656, 279936, 1679616, 10077696, 60466176, 362797056, 2176782336, 13060694016, 78364164096, 49, 343, 2401, 16807, 117649, 823543, 5764801, 40353607, 282475249, 1977326743, 13841287201, 96889010407, 678223072849, 64, 512, 4096, 32768, 262144, 2097152, 16777216, 134217728, 1073741824, 8589934592, 68719476736, 549755813888, 4398046511104, 81, 729, 6561, 59049, 531441, 4782969, 43046721, 387420489, 3486784401, 31381059609, 282429536481, 2541865828329, 22876792454961, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000, 10000000000, 100000000000, 1000000000000, 10000000000000, 100000000000000, 121, 1331, 14641, 161051, 1771561, 19487171, 214358881, 2357947691, 25937424601, 285311670611, 3138428376721, 34522712143931, 379749833583241, 144, 1728, 20736, 248832, 2985984, 35831808, 429981696, 5159780352, 61917364224, 743008370688, 8916100448256, 106993205379072, 1283918464548864, 169, 2197, 28561, 371293, 4826809, 62748517, 815730721, 10604499373, 137858491849, 1792160394037, 23298085122481, 302875106592253, 3937376385699289, 196, 2744, 38416, 537824, 7529536, 105413504, 1475789056, 20661046784, 289254654976, 4049565169664, 56693912375296, 793714773254144, 11112006825558016]
    # generated from
    # array = [[i ** j for j in range(2, 15)] for i in range(1, 15)]
    # for list in array:
    #     for element in list:
    #         powers.append(element)
    if n in powers:
        return True
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

    if list(factor_counter_dict.values()) == [1, 1]:
        return True
    return False

def fizzbuzz_extended(n):
    output = ''

    if n < 20:
        if n % 5 == 0 or '5' in str(n):
            output += 'bang '
        if n % 7 == 0 or '7' in str(n):
            output += 'buzz '
        if is_prime(n):
            output += 'crash '
        if is_fibonacci(n):
            output += 'fibbi '
        if not output:
            output = str(n)
    if n >= 20 and n < 40:
        if n % 5 == 0 or '5' in str(n):
            output += 'bang '
        if n % 7 == 0 or '7' in str(n):
            output += 'buzz '
        if is_prime(n):
            output += 'crash '
        if is_fibonacci(n):
            output += 'fibbi '
        if multiple_prime_factors(n):
            output += 'pop '
        if is_square_free(n):
            output += 'whizz'
        if is_a_power(n):
            output += 'zip '
        if not output:
            output = str(n)
    if n >= 40:
        if n % 5 == 0 or '5' in str(n):
            output += 'bang '
        if n % 7 == 0 or '7' in str(n):
            output += 'buzz '
        if is_prime(n):
            output += 'crash '
        if is_fibonacci(n):
            output += 'fibbi '
        if multiple_prime_factors(n):
            output += 'pop '
        if is_square_free(n):
            output += 'whizz'
        if is_a_power(n):
            output += 'zip '
        if is_sum_of_squares(n):
            output += 'squawk '
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
        await ctx.send('to play the game, type answer: then whatever buzz words apply to the number in chat (order doesnt matter). if ur right, the bot will continue; as you go on, more buzz words are gradually added. SPELLING MATTERS')

    @bot.command()
    async def fizzbuzz(ctx):

        if ctx.channel.name != 'fizz-buzz':
            await ctx.send("This game is only allowed in the 'fizz-buzz' channel.")
            return

        await ctx.send('Starting a new fizzbuzz round')

        for i in range(1, 1000):
            await ctx.send(f'current number: {i}')
            if i == 1:
                await ctx.send('starting on 1, the only buzz words in play are bang, buzz, crash, fibbi')
            elif i == 20:
                await ctx.send('in addition to bang, buzz, crash, and fibbi, pop, zip, and whizz are in play now')
            elif i == 40:
                await ctx.send('in addition to bang, buzz, crash, fibbi, pop, zip, and whizz, squawk and triple - the last two buzzwords - are in play now.')
            answer = fizzbuzz_extended(i)
            answer_list = answer.split(' ')
            print(answer)

            def check_message(message):
                return (
                        message.channel.name == 'fizz-buzz'
                        and message.author != bot.user
                        and message.content.startswith('answer: ')
                )

            user_answer = await bot.wait_for('message', check=check_message)
            user_answer_list = user_answer.content.split(' ')[1:]
            print(user_answer_list)

            if check_answers(user_answer_list, answer_list):
                await user_answer.add_reaction('✅')
            else:
                await user_answer.add_reaction('❌')
                await ctx.send('wrong! to restart the game, re-run the fizzbuzz command')
                break

    @bot.command()
    async def countdown(ctx):

        with open('questions.json', 'r') as file:
            questions = json.load(file)

        question_list = questions['questions']
        score = 0

        while True:
            random_question = random.choice(question_list)
            print(random_question['answer'])

            await ctx.send(random_question['url'])
            await ctx.send('you have 45 seconds to answer')

            def check_message(message, ctx):
                return (
                        message.channel.name == 'fizz-buzz'
                        and message.author != bot.user
                        and message.author == ctx.author
                )

            try:
                user_answer = await bot.wait_for('message', check=lambda message: check_message(message, ctx), timeout=45.0)
                if user_answer.content == random_question['answer']:
                    await user_answer.add_reaction('✅')
                    question_list.remove(random_question)
                    score += 1
                    print('length of list: ', str(len(question_list)))
                else:
                    await user_answer.add_reaction('❌')
            except asyncio.TimeoutError:
                await ctx.send('out of time! try again')
                continue

            if user_answer.content == "~end":
                await ctx.send('thanks for playing! you answered ' + str(score) + ' questions correctly')
                break


    bot.run('token')


if __name__ == '__main__':
    run()
