# The-first-project

## 대상 플랫폼
- Instagram (Reels)
- TikTok
- YouTube Shorts

## 공식 API / 파트너 프로그램 가능 여부
- **Instagram / Meta Graph API**
  - 공식 Graph API는 **비즈니스 또는 크리에이터 계정**이 필요하며, 앱은 Meta 검수를 거쳐야 합니다.
  - 게시물(예: Reels) 조회는 Graph API 범위 내에서 제공되는 필드에 한정됩니다.
- **TikTok for Developers API**
  - TikTok 공식 API 사용을 위해 개발자 계정 등록과 앱 승인 절차가 필요합니다.
  - 공개 콘텐츠 조회는 제공되는 엔드포인트 및 권한 범위 내에서만 가능합니다.
- **YouTube Shorts (YouTube Data API v3)**
  - YouTube Data API v3로 Shorts를 조회할 수 있으며, 프로젝트/키 발급 및 할당량 제한을 준수해야 합니다.

## “인기” 기준 (수치 정의)
- 좋아요 ≥ **5,000**
- 댓글 ≥ **200**
- 조회수 ≥ **100,000**

> 위 기준은 초기 가설 값이며, 실제 운영 시 플랫폼별 평균 지표에 맞춰 조정합니다.

## 동물 행동 영상 필터링 기준
- **키워드**
  - dog, puppy, cat, kitten, pet, animal, animals, puppycare, catcare
- **해시태그**
  - #dog, #puppy, #cat, #kitten, #pet, #animal, #animals, #pets, #dogvideo, #catvideo

## 허용되는 소스 + 필터 기준 (최종 요약)
- **허용 소스**
  - Instagram Reels (Meta Graph API)
  - TikTok (TikTok for Developers API)
  - YouTube Shorts (YouTube Data API v3)
- **필터 기준**
  - 인기: 좋아요 ≥ 5,000, 댓글 ≥ 200, 조회수 ≥ 100,000
  - 동물 행동: 키워드/해시태그 매칭 (상기 목록)
