from aiogram.dispatcher.filters.state import StatesGroup, State


class QRGeneratorStates(StatesGroup):
    WAIT_FOR_DATA_STATE = State()
