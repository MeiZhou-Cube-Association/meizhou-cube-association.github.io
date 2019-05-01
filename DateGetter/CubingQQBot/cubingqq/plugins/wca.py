import os
import sys
sys.path.append(os.path.abspath("../"))
from Spider import *

from nonebot import on_command, CommandSession

@on_command('wca')
async def weather(session: CommandSession):
    people = session.get('people', prompt='你想查谁？')

    wca_performance = await get_wca_performance(people)

    await session.send(wca_performance)


@weather.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state['people'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('要查的人，请重新输入')

    session.state[session.current_key] = stripped_arg


async def get_wca_performance(people: str) -> str:
    # print(f'{people}')
    name = f'{people}'
    print(name)
    msg = ProcessName(name)
    print(msg)
    return msg