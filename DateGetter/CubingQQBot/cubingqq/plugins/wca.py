import os
import sys
import pickle
sys.path.append(os.path.abspath("../"))
from Spider import *

from nonebot import on_command, CommandSession, on_natural_language,NLPSession, IntentCommand

@on_command('wca', only_to_me=False)
async def wca(session: CommandSession):
    people = session.get('people', prompt='你想查谁？')

    wca_performance = await get_wca_performance(people)
    if people == '余雷':
        await session.send("Lei Yu (余雷)\n2015YULE01\n三阶 1.23|0.15\n二阶 4.66|6.64\n四阶 1:01.88|1:11.11\n单手 27.36|31.48\n金字塔 5.24|8.78\n斜转 6.47|10.37")
    else:
        await session.send(wca_performance)


@wca.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state['people'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('要查的人，请重新输入')

    session.state[session.current_key] = stripped_arg
@on_natural_language(keywords={'-wca'}, only_to_me=False)
async def _(session: NLPSession):
    stripped_msg = session.msg_text.strip()
    people = stripped_msg.split("wca")[-1]
    # print(people)
    return IntentCommand(90.0, 'wca', current_arg=people)


async def get_wca_performance(people: str) -> str:
    # print(f'{people}')
    name = f'{people}'
    print(name)
    msg = ProcessName(name)
    # print(msg)
    return msg

# @on_command()