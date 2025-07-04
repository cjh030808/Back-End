from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from supabase import create_client, Client
from app.core.config import get_supabase_config

router = APIRouter()

# Supabase 클라이언트 초기화
SUPABASE_URL, SUPABASE_KEY = get_supabase_config()
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

@router.get("/leaderboard", response_class=JSONResponse)
async def get_leaderboard():
    try:
        # profiles 테이블에서 total_points 기준 내림차순 정렬, 상위 50명만 가져오기
        response = (
            supabase
            .table("profiles")
            .select("id, user_points, continuous_days, profile_image_url, profile")
            .order("user_points", desc=True)
            .limit(50)
            .execute()
        )
        if response.error:
            raise HTTPException(status_code=500, detail="DB 조회 중 오류가 발생했습니다.")
        leaderboard = response.data
        return {"leaderboard": leaderboard}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
