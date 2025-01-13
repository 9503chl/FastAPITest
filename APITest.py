from fastapi import FastAPI

from pydantic import BaseModel
from typing import Optional

class UserData(BaseModel):
    user_id: str
    user_name: str
    nickname: str
    character_type: str
    facial_expression_1: bytes = b"block(0)"
    facial_expression_2: bytes = b"block(0)"
    facial_expression_3: bytes = b"block(0)" 
    facial_expression_4: bytes = b"block(0)"
    material_texture_1: bytes = b"block(0)"
    material_texture_2: bytes = b"block(0)"
    material_texture_3: bytes = b"block(0)"
    material_texture_4: bytes = b"block(0)"
    material_texture_5: bytes = b"block(0)"
    screenshot_image: bytes = b"block(0)"
    third_name: str
    effect_name: str
    bg_name: str
    scenario_text: str
    motion_data_1: bytes = b"block(0)"
    motion_data_2: bytes = b"block(0)" 
    motion_data_3: bytes = b"block(0)"
    motion_data_4: bytes = b"block(0)"
    motion_data_5: bytes = b"block(0)"
    video_file: bytes = b"block(0)"
    effect_url: str

app = FastAPI()

@app.get("/users/{user_id}")
async def get_user(user_id: str):
    # 실제 구현에서는 데이터베이스 조회 로직이 들어갈 것입니다
    # 현재는 예시 데이터를 반환합니다
    user_data = UserData(
        user_id=user_id,
        user_name="테스트 사용자",
        nickname="닉네임",
        character_type="기본",
        third_name="third_name",
        effect_name="effect_name", 
        bg_name="bg_name",
        scenario_text="시나리오 텍스트",
        effect_url="effect_url"
    )
    return user_data
