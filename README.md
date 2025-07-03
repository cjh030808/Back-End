backend/
├── app/                      # FastAPI 소스코드의 메인 디렉토리
│   ├── main.py               # FastAPI 앱의 시작점. 앱 인스턴스 생성, 미들웨어/라우터 포함
│   ├── api/                  # API 엔드포인트(라우터)들을 모아두는 곳
│   │   └── v1/               # API 버전 관리 (v1, v2 등)
│   │       ├── router.py     # v1의 모든 엔드포인트 라우터들을 통합하는 파일
│   │       └── endpoints/    # 기능별 엔드포인트 파일
│   │           ├── __init__.py
│   │           ├── users.py      # 사용자 프로필, 포인트 조회 등
│   │           ├── verification.py # 3가지 인증 방식(사진, 퀴즈, 소감문) 처리
│   │           ├── characters.py # AI 캐릭터 생성
│   │           └── community.py  # 커뮤니티(게시글, 좋아요, 댓글)
│   │
│   ├── core/                 # 프로젝트의 핵심 설정
│   │   └── config.py         # 환경변수, 시크릿 키 등 설정 관리
│   │
│   ├── services/             # 비즈니스 로직
│   │   ├── generate/
│   │   │   ├── character
│   │   │   ├── article
│   │   │   └── quiz
│   │   └── verify/
│   │   │   ├── image
│   │   │   ├── article
│   │   │   └── quiz
│   │
│   └── utils/                # 여러 곳에서 사용되는 유틸리티 함수
│       ├── util.py
│       └── exceptions.py     # 커스텀 예외 처리
│
├── .env                      # 환경변수 파일 (DB 접속 정보, API 키 등). 절대로 Git에 올리면 안 됨!
├── .gitignore                # Git 추적 제외 목록
└── requirements.txt          # 프로젝트 의존성 패키지 목록
