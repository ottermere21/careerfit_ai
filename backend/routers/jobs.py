from fastapi import APIRouter
from typing import List

router = APIRouter()

# 목업 데이터: 3일차에 실제 CSV 데이터로 교체한다
MOCK_JOBS = [
    {
        "id": 1,
        "company": "테크스타트업A",
        "title": "데이터 분석가",
        "required_skills": ["Python", "SQL", "통계"],
        "preferred_skills": ["R", "Tableau", "머신러닝"],
        "description": "사용자 행동 데이터를 분석해 비즈니스 인사이트를 도출합니다.",
        "deadline": "2026-07-31"
    },
    {
        "id": 2,
        "company": "금융서비스B",
        "title": "백엔드 개발자",
        "required_skills": ["Python", "FastAPI", "PostgreSQL"],
        "preferred_skills": ["Docker", "AWS", "Redis"],
        "description": "금융 데이터 처리 API 서버를 개발하고 운영합니다.",
        "deadline": "2026-08-15"
    },
    {
        "id": 3,
        "company": "공공기관C",
        "title": "AI 연구원",
        "required_skills": ["Python", "딥러닝", "PyTorch"],
        "preferred_skills": ["논문 작성", "NLP", "컴퓨터 비전"],
        "description": "공공 서비스 개선을 위한 AI 모델을 연구·개발합니다.",
        "deadline": "2026-08-01"
    },
    {
        "id": 4,
        "company": "우아한형제들",
        "title": "주니어 백엔드 개발자 (주문 시스템)",
        "required_skills": ["Java", "Spring Boot", "MySQL"],
        "preferred_skills": ["JPA", "Docker"],
        "description": "대용량 트래픽을 처리하는 주문 및 결제 API를 설계하고 개발합니다. 컴퓨터과학적 기초를 기반으로 확장 가능하고 효율적인 백엔드 아키텍처를 구축합니다.",
        "deadline": "2026-08-31"
    },
    {
        "id": 5,
        "company": "토스페이먼츠",
        "title": "백엔드 개발자 (결제 플랫폼)",
        "required_skills": ["Kotlin", "Spring Boot", "PostgreSQL"],
        "preferred_skills": ["Redis", "Kafka"],
        "description": "안정적이고 신뢰할 수 있는 통합 결제 API 서버 시스템을 설계하고 운영합니다. 트랜잭션의 정확성과 동시성 제어 문제를 주로 다룹니다.",
        "deadline": "2026-08-31"
    },
    {
        "id": 6,
        "company": "당근마켓",
        "title": "백엔드 엔지니어 (지역 서비스)",
        "required_skills": ["Python", "FastAPI", "PostgreSQL"],
        "preferred_skills": ["AWS", "Kubernetes"],
        "description": "지역 서비스의 신규 기능 API 및 실시간 데이터 처리 서버를 빠르게 개발합니다. 병목 지점을 최적화하고 컨테이너 기반 인프라를 조율합니다.",
        "deadline": "2026-08-31"
    },
    {
        "id": 7,
        "company": "네이버",
        "title": "백엔드 개발자 (검색 플랫폼)",
        "required_skills": ["Java", "Spring Boot", "MySQL"],
        "preferred_skills": ["Redis", "Elasticsearch"],
        "description": "네이버 검색 서비스의 안정적인 대용량 트래픽 처리를 위한 백엔드 시스템을 개발합니다. 분산 환경에서의 데이터 동기화와 고성능 검색 인덱싱 파이프라인을 구축합니다.",
        "deadline": "2026-08-31"
    },
    {
        "id": 8,
        "company": "카카오",
        "title": "백엔드 엔지니어 (카카오페이)",
        "required_skills": ["Kotlin", "Spring Boot", "JPA"],
        "preferred_skills": ["Kafka", "Docker"],
        "description": "카카오페이 결제 및 정산 시스템의 백엔드 API를 개발하고 운영합니다. 대용량 트랜잭션 상황에서도 데이터의 정합성을 보장하는 고신뢰성 금융 플랫폼을 지향합니다.",
        "deadline": "2026-08-31"
    },
    {
        "id": 9,
        "company": "라인플러스",
        "title": "주니어 백엔드 엔지니어 (메시징 서버)",
        "required_skills": ["Java", "Spring Boot", "MySQL"],
        "preferred_skills": ["Redis", "Kubernetes"],
        "description": "글로벌 라인 사용자를 위한 대용량 실시간 메시징 서버 아키텍처를 설계하고 고도화합니다. 컴퓨터과학 기본기를 활용하여 대규모 트래픽 병목 현상을 해결합니다.",
        "deadline": "2026-08-31"
    }
]

@router.get("/jobs", tags=["Jobs"])
def get_jobs():
    """
    취업 공고 목록을 반환하는 엔드포인트.
    현재는 목업 데이터를 반환하며, 3일차에 실제 데이터로 교체한다.
    """
    return {
        "count": len(MOCK_JOBS),
        "jobs": MOCK_JOBS
    }


@router.get("/jobs/{job_id}", tags=["Jobs"])
def get_job_by_id(job_id: int):
    """
    특정 공고의 상세 정보를 반환한다.
    """
    for job in MOCK_JOBS:
        if job["id"] == job_id:
            return job
    # 찾지 못한 경우
    from fastapi import HTTPException
    raise HTTPException(status_code=404, detail=f"공고 ID {job_id}를 찾을 수 없습니다.")