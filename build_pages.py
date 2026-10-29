import os
import itertools
import urllib.parse

BASE_URL = "https://nuagyeol1004.netlify.app"
PHONE = "0507-1280-3199"
BRAND_NAME = "누아결1004"
YOUTUBE_ID = "DxwimcJq3_A"

# 3종 키워드 로테이션 (SEO 중복 방지)
KEYWORD_ROTATION = itertools.cycle([
    "출장 베스트 마사지",
    "출장 VIP케어 마사지",
    "출장 어울림 마사지"
])

# 지역별 추천 제휴업체 5개 풀
SHOPS_DATA = [
    {
        "name": "오늘밤테라피",
        "tag": "인기 1위",
        "badge": "★추천",
        "desc": "선입금 없는 100% 안심 후불제! 타이, 전신아로마 및 VIP 감성힐링 전문",
        "price": "60,000원부터~",
        "score": "4.9",
        "reviews": "148",
        "img": "/images/shop1.jpg"
    },
    {
        "name": "한국미인홈케어",
        "tag": "한국인 힐러",
        "badge": "전문케어",
        "desc": "지친 일상에 맞춤형 피로회복 케어! 베테랑 한국인 테라피스트의 프라이빗 릴렉싱",
        "price": "70,000원부터~",
        "score": "4.9",
        "reviews": "112",
        "img": "/images/shop2.jpg"
    },
    {
        "name": "주주테라피",
        "tag": "스웨디시",
        "badge": "위생철저",
        "desc": "재방문율 높은 안심 케어! 철저한 위생 관리와 최고급 럭셔리 스웨디시 프로그램",
        "price": "60,000원부터~",
        "score": "4.8",
        "reviews": "95",
        "img": "/images/shop3.jpg"
    },
    {
        "name": "퀸즈홈테라피",
        "tag": "VIP 케어",
        "badge": "맞춤체형",
        "desc": "전문 힐러진의 체형 맞춤 피로회복 특화 프로그램 및 천연 에센셜 오일 관리",
        "price": "80,000원부터~",
        "score": "4.9",
        "reviews": "130",
        "img": "/images/shop4.jpg"
    },
    {
        "name": "골든테라피",
        "tag": "신속방문",
        "badge": "25분 도착",
        "desc": "선입금 전혀 없는 100% 후불제! 수도권 각 구마다 상주 기사 25분 내 신속 방문",
        "price": "90,000원부터~",
        "score": "4.8",
        "reviews": "88",
        "img": "/images/shop5.jpg"
    }
]

REGION_DATA = {
    'seoul': {
        'name': '서울',
        'districts': {
            'jongno': {'name': '종로구', 'dongs': ['청운동', '효자동', '사직동', '삼청동', '부암동', '평창동', '무악동', '교남동', '가회동', '종로1.2.3.4가동', '종로5.6가동', '이화동', '혜화동', '창신1동', '창신2동', '창신3동', '숭인1동', '숭인2동']},
            'jung': {'name': '중구', 'dongs': ['소공동', '회현동', '명동', '필동', '장충동', '광희동', '을지로동', '신당동', '다산동', '약수동', '청구동', '동화동', '황학동', '중림동']},
            'yongsan': {'name': '용산구', 'dongs': ['후암동', '용산2가동', '남영동', '청파동', '원효로1동', '원효로2동', '효창동', '용문동', '이촌1동', '이촌2동', '이태원1동', '이태원2동', '한남동', '서빙고동', '보광동']},
            'seongdong': {'name': '성동구', 'dongs': ['왕십리2동', '왕십리도선동', '마장동', '사근동', '행당1동', '행당2동', '응봉동', '금호1가동', '금호2.3가동', '금호4가동', '옥수동', '성수1가1동', '성수1가2동', '성수2가1동', '성수2가3동', '송정동', '용답동']},
            'gwangjin': {'name': '광진구', 'dongs': ['중곡1동', '중곡2동', '중곡3동', '중곡4동', '능동', '구의1동', '구의2동', '구의3동', '광장동', '자양1동', '자양2동', '자양3동', '자양4동', '화양동', '군자동']},
            'dongdaemun': {'name': '동대문구', 'dongs': ['신설동', '용두동', '제기동', '전농1동', '전농2동', '답십리1동', '답십리2동', '장안1동', '장안2동', '청량리동', '회기동', '휘경1동', '휘경2동', '이문1동', '이문2동']},
            'jungnang': {'name': '중랑구', 'dongs': ['면목본동', '면목2동', '면목3.4동', '면목5동', '면목7동', '상봉1동', '상봉2동', '중화1동', '중화2동', '묵1동', '묵2동', '망우본동', '망우3동', '신내1동', '신내2동']},
            'seongbuk': {'name': '성북구', 'dongs': ['성북동', '삼선동', '동선동', '돈암1동', '돈암2동', '안암동', '보문동', '정릉1동', '정릉2동', '정릉3동', '정릉4동', '길음1동', '길음2동', '종암동', '월곡1동', '월곡2동', '장위1동', '장위2동', '장위3동', '석관동']},
            'gangbuk': {'name': '강북구', 'dongs': ['삼양동', '미아동', '송중동', '송천동', '삼각산동', '번1동', '번2동', '번3동', '수유1동', '수유2동', '수유3동', '우이동', '인수동']},
            'dobong': {'name': '도봉구', 'dongs': ['창1동', '창2동', '창3동', '창4동', '창5동', '도봉1동', '도봉2동', '쌍문1동', '쌍문2동', '쌍문3동', '쌍문4동', '방학1동', '방학2동', '방학3동']},
            'nowon': {'name': '노원구', 'dongs': ['상계1동', '상계2동', '상계3.4동', '상계5동', '상계6.7동', '상계8동', '상계9동', '상계10동', '중계본동', '중계1동', '중계2.3동', '중계4동', '하계1동', '하계2동', '공릉1동', '공릉2동']},
            'eunpyeong': {'name': '은평구', 'dongs': ['불광1동', '불광2동', '갈현1동', '갈현2동', '구산동', '대조동', '응암1동', '응암2동', '응암3동', '역촌동', '신사1동', '신사2동', '증산동', '수색동', '진관동']},
            'seodaemun': {'name': '서대문구', 'dongs': ['천연동', '북아현동', '충현동', '신촌동', '연희동', '홍제1동', '홍제2동', '홍제3동', '홍은1동', '홍은2동', '남가좌1동', '남가좌2동', '북가좌1동', '북가좌2동']},
            'mapo': {'name': '마포구', 'dongs': ['공덕동', '아현동', '도화동', '용강동', '대흥동', '염리동', '신수동', '서교동', '합정동', '망원1동', '망원2동', '연남동', '성산1동', '성산2동', '상암동']},
            'yangcheon': {'name': '양천구', 'dongs': ['목1동', '목2동', '목3동', '목4동', '목5동', '신월1동', '신월2동', '신월3동', '신월4동', '신월5동', '신월6동', '신월7동', '신정1동', '신정2동', '신정3동', '신정4동', '신정6동', '신정7동']},
            'gangseo': {'name': '강서구', 'dongs': ['등촌1동', '등촌2동', '등촌3동', '화곡본동', '화곡1동', '화곡2동', '화곡3동', '화곡4동', '화곡8동', '우장산동', '가양1동', '가양2동', '가양3동', '발산1동', '공항동', '방화1동', '방화2동', '방화3동']},
            'guro': {'name': '구로구', 'dongs': ['신도림동', '구로1동', '구로2동', '구로3동', '구로4동', '구로5동', '가리봉동', '고척1동', '고척2동', '개봉1동', '개봉2동', '개봉3동', '오류1동', '오류2동', '수궁동']},
            'geumcheon': {'name': '금천구', 'dongs': ['가산동', '독산1동', '독산2동', '독산3동', '독산4동', '시흥1동', '시흥2동', '시흥3동', '시흥4동', '시흥5동']},
            'yeongdeungpo': {'name': '영등포구', 'dongs': ['영등포본동', '영등포동', '여의동', '당산1동', '당산2동', '도림동', '문래동', '양평1동', '양평2동', '신길1동', '신길3동', '신길4동', '신길5동', '신길6동', '신길7동', '대림1동', '대림2동', '대림3동']},
            'dongjak': {'name': '동작구', 'dongs': ['노량진1동', '노량진2동', '상도1동', '상도2동', '상도3동', '상도4동', '흑석동', '사당1동', '사당2동', '사당3동', '사당4동', '사당5동', '대방동', '신대방1동', '신대방2동']},
            'gwanak': {'name': '관악구', 'dongs': ['보라매동', '청림동', '성현동', '행운동', '낙성대동', '청룡동', '은천동', '상현동', '서원동', '신원동', '서림동', '신사동', '난향동', '조원동', '대학동', '난곡동', '삼성동', '미성동']},
            'seocho': {'name': '서초구', 'dongs': ['서초1동', '서초2동', '서초3동', '서초4동', '잠원동', '반포본동', '반포1동', '반포2동', '반포3동', '반포4동', '방배본동', '방배1동', '방배2동', '방배3동', '방배4동', '양재1동', '양재2동', '내곡동']},
            'gangnam': {'name': '강남구', 'dongs': ['역삼1동', '역삼2동', '개포1동', '개포2동', '개포4동', '청담동', '삼성1동', '삼성2동', '대치1동', '대치2동', '대치4동', '신사동', '논현1동', '논현2동', '압구정동', '세곡동', '자곡동', '일원동', '수서동', '도곡1동', '도곡2동']},
            'songpa': {'name': '송파구', 'dongs': ['잠실본동', '잠실2동', '잠실3동', '잠실4동', '잠실6동', '잠실7동', '풍납1동', '풍납2동', '거여1동', '거여2동', '마천1동', '마천2동', '방이1동', '방이2동', '오륜동', '오금동', '송파1동', '송파2동', '석촌동', '삼전동', '가락본동', '가락1동', '가락2동', '문정1동', '문정2동', '장지동', '위례동', '잠실동']},
            'gangdong': {'name': '강동구', 'dongs': ['강일동', '상일1동', '상일2동', '명일1동', '명일2동', '고덕1동', '고덕2동', '암사1동', '암사2동', '암사3동', '천호1동', '천호2동', '천호3동', '성내1동', '성내2동', '성내3동', '둔촌1동', '둔촌2동']}
        }
    },
    'incheon': {
        'name': '인천',
        'districts': {
            'jemulpo': {'name': '제물포구', 'dongs': ['신포동', '연안동', '신흥동', '도원동', '율목동', '동인천동', '개항동', '만석동', '화수동', '송현동', '송림동', '금창동']},
            'yeongjong': {'name': '영종구', 'dongs': ['영종동', '영종1동', '영종2동', '운서동', '용유동', '중산동', '운남동', '운북동']},
            'michuhol': {'name': '미추홀구', 'dongs': ['숭의동', '용현동', '학익동', '도화동', '주안동', '관교동', '문학동']},
            'yeonsu': {'name': '연수구', 'dongs': ['옥련동', '선학동', '연수동', '청학동', '동춘동', '송도1동', '송도2동', '송도3동', '송도4동', '송도5동']},
            'namdong': {'name': '남동구', 'dongs': ['구월동', '간석동', '만수동', '장수서창동', '서창동', '남촌도림동', '논현동', '논현고잔동']},
            'bupyeong': {'name': '부평구', 'dongs': ['부평동', '산곡동', '청천동', '갈산동', '삼산동', '부개동', '일신동', '십정동']},
            'gyeyang': {'name': '계양구', 'dongs': ['효성동', '계산동', '작전동', '작전서운동', '계양동']},
            'seohae': {'name': '서구', 'dongs': ['검암경서동', '연희동', '청라1동', '청라2동', '청라3동', '가정동', '신현원창동', '석남동', '가좌동']},
            'geomdan': {'name': '검단구', 'dongs': ['검단동', '불로대곡동', '원당동', '당하동', '오류왕길동', '마전동', '아라동', '금곡동']},
            'ganghwa': {'name': '강화군', 'dongs': ['강화읍', '선원면', '불은면', '길상면', '화도면', '양도면', '내가면', '하점면', '양사면', '송해면', '교동면', '삼산면', '서도면']},
            'ongjin': {'name': '옹진군', 'dongs': ['북도면', '연평면', '백령면', '대청면', '덕적면', '자월면', '영흥면']}
        }
    },
    'gyeonggi': {
        'name': '경기',
        'districts': {
            'suwon_paldal': {'name': '수원시 팔달구', 'dongs': ['매교동', '매산동', '고등동', '화서1동', '화서2동', '지동', '우만1동', '우만2동', '인계동']},
            'seongnam_bundang': {'name': '성남시 분당구', 'dongs': ['분당동', '수내동', '정자동', '서현동', '이매동', '야탑동', '금곡동', '구미동', '판교동', '삼평동', '백현동', '운중동']},
            'bucheon_wonmi': {'name': '부천시 원미구', 'dongs': ['심곡동', '원미동', '소사동', '역곡동', '중동', '상동', '약대동']},
            'goyang_ilsandong': {'name': '고양시 일산동구', 'dongs': ['식사동', '중산동', '정발산동', '풍산동', '백석동', '마두동', '장항동', '고봉동']}
        }
    }
}

HTML_TEMPLATE = """<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <meta name="robots" content="index,follow,max-image-preview:large">
  <meta name="Yeti" content="index,follow,max-image-preview:large">
  <title>{page_title}</title>
  <meta name="description" content="{meta_description}">
  <link rel="canonical" href="{canonical_url}">
  
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="{brand}">
  <meta property="og:title" content="{page_title}">
  <meta property="og:description" content="{meta_description}">
  <meta property="og:url" content="{canonical_url}">
  <meta property="og:image" content="https://images.unsplash.com/photo-1540555700478-4be289fbecef?auto=format&fit=crop&w=1200&h=630&q=80">

  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "LocalBusiness",
    "name": "{page_title_h1} - {brand}",
    "description": "{meta_description}",
    "url": "{canonical_url}",
    "telephone": "{phone}",
    "priceRange": "60,000원 ~ 180,000원",
    "aggregateRating": {{
      "@type": "AggregateRating",
      "ratingValue": "4.9",
      "reviewCount": "148",
      "bestRating": "5",
      "worstRating": "1"
    }}
  }}
  </script>

  <style>
    :root {{
      --bg-dark: #121013;
      --card-bg: #1c181d;
      --card-inner: #151218;
      --card-border: #2c252f;
      --text-main: #f3eff5;
      --text-muted: #9e93a2;
      --accent-pink: #c76f8e;
      --accent-pink-hover: #db7d9e;
      --accent-box-bg: #9e4b6c;
      --accent-box-btn: #f7dbe3;
      --accent-box-btn-text: #742542;
      --star-color: #f59e0b;
      --font-family: -apple-system, BlinkMacSystemFont, "Apple SD Gothic Neo", "Pretendard", Roboto, "Noto Sans KR", sans-serif;
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{ background-color: var(--bg-dark); color: var(--text-main); font-family: var(--font-family); line-height: 1.6; padding-bottom: 70px; }}
    a {{ color: inherit; text-decoration: none; }}
    .wrap {{ max-width: 1140px; margin: 0 auto; padding: 0 16px; }}
    header.top {{ border-bottom: 1px solid var(--card-border); background: rgba(18, 16, 19, 0.96); position: sticky; top: 0; z-index: 100; backdrop-filter: blur(8px); }}
    .header-row {{ display: flex; align-items: center; justify-content: space-between; height: 64px; }}
    .brand {{ font-size: 1.35rem; font-weight: 800; letter-spacing: -0.5px; color: #fff; }}
    .brand span {{ color: var(--accent-pink); }}
    .nav {{ display: flex; gap: 14px; font-size: 0.9rem; font-weight: 600; }}
    .page-head {{ padding: 24px 0 16px; }}
    .breadcrumbs {{ font-size: 0.82rem; color: var(--text-muted); margin-bottom: 8px; }}
    .breadcrumbs a:hover {{ text-decoration: underline; color: var(--accent-pink); }}
    .title-line h1 {{ font-size: 1.75rem; font-weight: 800; margin-bottom: 4px; }}
    .star-summary-bar {{ display: inline-flex; align-items: center; gap: 8px; background: var(--card-inner); border: 1px solid var(--card-border); padding: 6px 14px; border-radius: 20px; font-size: 0.85rem; margin-top: 10px; }}
    .star-summary-bar .stars {{ color: var(--star-color); font-weight: bold; }}
    .tags {{ display: flex; flex-wrap: wrap; gap: 8px; margin: 16px 0 24px; }}
    .tag {{ background: var(--card-inner); border: 1px solid var(--card-border); padding: 6px 14px; border-radius: 20px; font-size: 0.85rem; transition: 0.2s; }}
    .tag:hover {{ border-color: var(--accent-pink); color: #fff; background: var(--accent-pink); }}
    .detail-layout {{ display: grid; grid-template-columns: 1fr 310px; gap: 24px; align-items: start; }}
    .panel {{ background: var(--card-bg); border: 1px solid var(--card-border); border-radius: 12px; padding: 24px; margin-bottom: 20px; }}
    .panel h2 {{ font-size: 1.25rem; font-weight: 700; margin-bottom: 16px; color: #fff; }}
    .course-table {{ width: 100%; border-collapse: collapse; text-align: left; font-size: 0.92rem; }}
    .course-table th, .course-table td {{ padding: 12px 14px; border-bottom: 1px solid var(--card-border); }}
    .course-table th {{ color: var(--text-muted); font-weight: 600; background: var(--card-inner); }}
    .course-table td:last-child {{ font-weight: 700; text-align: right; color: #fff; }}
    .course-badge {{ font-size: 0.72rem; padding: 2px 6px; border-radius: 4px; margin-left: 6px; background: rgba(199, 111, 142, 0.2); color: var(--accent-pink); font-weight: bold; }}
    .shop-list {{ display: flex; flex-direction: column; gap: 14px; margin-bottom: 24px; }}
    .shop-card-item {{ background: var(--card-inner); border: 1px solid var(--card-border); border-radius: 12px; padding: 16px; display: flex; gap: 16px; align-items: center; transition: 0.2s; }}
    .shop-card-item:hover {{ border-color: var(--accent-pink); transform: translateY(-2px); }}
    .shop-card-item img {{ width: 100px; height: 100px; object-fit: cover; border-radius: 8px; flex-shrink: 0; }}
    .shop-card-info {{ flex: 1; min-width: 0; }}
    .shop-card-info h3 {{ font-size: 1.05rem; font-weight: 800; color: #fff; margin-bottom: 4px; display: flex; align-items: center; gap: 8px; }}
    .shop-card-info p {{ font-size: 0.82rem; color: var(--text-muted); margin-bottom: 6px; line-height: 1.4; }}
    .shop-card-bottom {{ display: flex; justify-content: space-between; align-items: center; }}
    .shop-card-bottom .price {{ color: var(--star-color); font-weight: 800; font-size: 0.95rem; }}
    .call-btn-mini {{ background: var(--accent-pink); color: #fff; padding: 6px 14px; border-radius: 6px; font-size: 0.82rem; font-weight: bold; }}
    .map-frame, .video-frame {{ width: 100%; height: 280px; border: 0; border-radius: 8px; margin-top: 12px; }}
    .profile-summary {{ background: var(--accent-box-bg); padding: 24px; border-radius: 14px; position: sticky; top: 84px; color: #fff; box-shadow: 0 4px 20px rgba(0,0,0,0.3); }}
    .profile-summary small {{ font-size: 0.85rem; opacity: 0.9; }}
    .profile-summary .price {{ font-size: 1.9rem; font-weight: 800; margin: 8px 0 14px; }}
    .profile-summary .price small {{ font-size: 1rem; font-weight: 400; }}
    .profile-summary p {{ font-size: 0.88rem; line-height: 1.45; opacity: 0.95; margin-bottom: 20px; }}
    .profile-call {{ display: block; width: 100%; background: var(--accent-box-btn); color: var(--accent-box-btn-text); text-align: center; padding: 12px 0; border-radius: 8px; font-size: 1rem; font-weight: 800; }}
    .fixed-call {{ position: fixed; bottom: 0; left: 0; right: 0; height: 54px; background: var(--accent-pink); color: #fff; display: flex; align-items: center; justify-content: center; font-size: 1.05rem; font-weight: 700; z-index: 999; box-shadow: 0 -2px 10px rgba(0,0,0,0.5); }}
    footer {{ border-top: 1px solid var(--card-border); padding: 30px 0; text-align: center; color: var(--text-muted); font-size: 0.85rem; }}
    @media (max-width: 900px) {{
      .detail-layout {{ grid-template-columns: 1fr; }}
      .profile-summary {{ position: static; margin-bottom: 24px; }}
      .shop-card-item {{ flex-direction: column; align-items: flex-start; }}
      .shop-card-item img {{ width: 100%; height: 160px; }}
    }}
  </style>
</head>
<body class="design-suwon-layout-04-dark-luxury">
  <header class="top">
    <div class="wrap header-row">
      <a class="brand" href="/">{brand}<span>.</span></a>
      <nav class="nav">
        <a href="/">메인 홈</a>
        <a href="tel:{phone}">전화 상담</a>
      </nav>
    </div>
  </header>

  <main id="main">
    <div class="wrap">
      <div class="page-head">
        <div class="breadcrumbs">{breadcrumbs}</div>
        <div class="title-line">
          <h1>{page_title_h1}</h1>
          <p class="page-description">선입금 없는 100% 안심 후불제! {location_title} 베스트 제휴업체 코스와 예약 정보를 확인하세요.</p>
        </div>
        <div class="star-summary-bar">
          <span class="stars">★★★★★ 4.9</span>
          <span>|</span>
          <span>제휴업체 <strong>5개점 입점</strong></span>
          <span>|</span>
          <span style="color: #6ee7b7;">선입금 0원 보장</span>
        </div>
      </div>

      {tag_section}

      <div class="detail-layout">
        <div>
          <!-- 1. 지역 추천 제휴업체 5개점 목록 -->
          <section class="panel">
            <h2>{location_title} 추천 제휴업체 안내 (5곳)</h2>
            <div class="shop-list">
              {shop_cards_html}
            </div>
          </section>

          <!-- 2. 오늘밤테라피 기준 표준 코스/가격표 -->
          <section class="panel">
            <h2>{location_title} 표준 코스·가격표 (오늘밤테라피 기준)</h2>
            <table class="course-table">
              <thead>
                <tr><th>코스 프로그램</th><th>시간</th><th>가격</th></tr>
              </thead>
              <tbody>
                <tr><td>🔮 타이코스</td><td>60분 / 90분 / 120분</td><td>60,000원 ~ 100,000원</td></tr>
                <tr><td>🔮 전신아로마</td><td>60분 / 90분 / 120분</td><td>70,000원 ~ 110,000원</td></tr>
                <tr><td>🔮 VIP 감성힐링코스 <span class="course-badge">★추천</span></td><td>60분 / 90분 / 120분</td><td>90,000원 ~ 130,000원</td></tr>
                <tr><td>🔮 VIP 스페셜코스 <span class="course-badge">★추천</span></td><td>60분 / 90분 / 120분</td><td>100,000원 ~ 140,000원</td></tr>
                <tr><td>🔮 VIP 프리미엄 코스 (풀패키지)</td><td>150분</td><td>160,000원</td></tr>
                <tr><td>🔮 한국인스웨디시</td><td>60분 / 90분</td><td>140,000원 ~ 180,000원</td></tr>
              </tbody>
            </table>
          </section>

          <!-- 3. 지도 및 유튜브 영상 -->
          <section class="panel">
            <h2>{location_title} 위치 및 안내 영상</h2>
            <iframe class="map-frame" loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="https://www.google.com/maps?q={map_query}&output=embed" title="{location_title} 지도"></iframe>
            <iframe class="video-frame" loading="lazy" src="https://www.youtube-nocookie.com/embed/{youtube_id}" title="누아결1004 이용 안내 영상" allowfullscreen></iframe>
          </section>
        </div>

        <aside class="profile-summary">
          <small>{location_title} · 누아결1004</small>
          <div class="price">60,000원<small>부터</small></div>
          <p>선입금 없는 100% 안심 후불제! 입점 업체와 원하는 코스를 지금 바로 상담하세요.</p>
          <a class="profile-call" href="tel:{phone}">실시간 제휴 상담 ({phone})</a>
        </aside>
      </div>
    </div>
  </main>

  <footer>
    <div class="wrap">
      <p>© 2026 {brand}. All Rights Reserved. 상담 번호: {phone}</p>
    </div>
  </footer>

  <a class="fixed-call" href="tel:{phone}">실시간 제휴업체 상담 ({phone})</a>
</body>
</html>
"""

def generate_shop_cards(location_name):
    cards = []
    for shop in SHOPS_DATA:
        card = f"""
        <div class="shop-card-item">
          <img src="{shop['img']}" alt="{location_name} {shop['name']}">
          <div class="shop-card-info">
            <h3>{shop['name']} <span style="font-size:0.75rem; color:#f59e0b;">★ {shop['score']}</span> <span style="font-size:0.7rem; background:rgba(245,158,11,0.2); color:#f59e0b; padding:2px 6px; border-radius:4px;">{shop['tag']}</span></h3>
            <p>{shop['desc']}</p>
            <div class="shop-card-bottom">
              <span class="price">{shop['price']}</span>
              <a class="call-btn-mini" href="tel:{PHONE}">전화예약</a>
            </div>
          </div>
        </div>
        """
        cards.append(card)
    return "".join(cards)

def make_page(path, html_content):
    os.makedirs(path, exist_ok=True)
    with open(os.path.join(path, "index.html"), "w", encoding="utf-8") as f:
        f.write(html_content)

urls = [f"{BASE_URL}/"]

print("누아결1004 다중 업체 페이지 생성을 시작합니다...")

for reg_key, reg_val in REGION_DATA.items():
    reg_name = reg_val['name']
    
    # 1. 시/도 페이지
    current_kw = next(KEYWORD_ROTATION)
    reg_dir = os.path.join("region", reg_key)
    reg_url = f"{BASE_URL}/region/{reg_key}/"
    urls.append(reg_url)
    
    p_title = f"{reg_name} 출장 {current_kw} 제휴업체 목록 | {BRAND_NAME}"
    m_desc = f"{reg_name} 출장 베스트 마사지 업체와 코스 정보를 누아결1004 에서 편리하게 확인하세요. 실시간 전화상담 {PHONE}"
    
    dist_tags = "".join([f'<a class="tag" href="/region/{reg_key}/{d_key}/">{d_val["name"]}</a>' for d_key, d_val in reg_val['districts'].items()])
    tag_html = f'<div class="tags">{dist_tags}</div>'
    
    make_page(reg_dir, HTML_TEMPLATE.format(
        brand=BRAND_NAME, phone=PHONE, youtube_id=YOUTUBE_ID,
        map_query=urllib.parse.quote(reg_name),
        page_title=p_title,
        page_title_h1=f"{reg_name} 출장 {current_kw}",
        meta_description=m_desc,
        location_title=reg_name,
        canonical_url=reg_url,
        breadcrumbs=f'홈 › <a href="/">지역별</a> › {reg_name}',
        tag_section=tag_html,
        shop_cards_html=generate_shop_cards(reg_name)
    ))
    
    # 2. 구/군 페이지
    for dist_key, dist_val in reg_val['districts'].items():
        dist_name = dist_val['name']
        current_kw = next(KEYWORD_ROTATION)
        dist_dir = os.path.join(reg_dir, dist_key)
        dist_url = f"{BASE_URL}/region/{reg_key}/{dist_key}/"
        urls.append(dist_url)
        
        full_dist_title = f"{reg_name} {dist_name}"
        p_title = f"{full_dist_title} 출장 {current_kw} 제휴업체 목록 | {BRAND_NAME}"
        m_desc = f"{full_dist_title} 출장 베스트 마사지 업체와 코스 정보를 누아결1004 에서 편리하게 확인하세요. 실시간 전화상담 {PHONE}"
        
        dong_tags = "".join([f'<a class="tag" href="/region/{reg_key}/{dist_key}/{urllib.parse.quote(d)}/">{d}</a>' for d in dist_val['dongs']])
        tag_html = f'<div class="tags">{dong_tags}</div>'
        
        make_page(dist_dir, HTML_TEMPLATE.format(
            brand=BRAND_NAME, phone=PHONE, youtube_id=YOUTUBE_ID,
            map_query=urllib.parse.quote(full_dist_title),
            page_title=p_title,
            page_title_h1=f"{full_dist_title} 출장 {current_kw}",
            meta_description=m_desc,
            location_title=full_dist_title,
            canonical_url=dist_url,
            breadcrumbs=f'홈 › <a href="/region/{reg_key}/">{reg_name}</a> › {dist_name}',
            tag_section=tag_html,
            shop_cards_html=generate_shop_cards(full_dist_title)
        ))
        
        # 3. 동/읍/면 페이지
        for dong in dist_val['dongs']:
            current_kw = next(KEYWORD_ROTATION)
            dong_dir = os.path.join(dist_dir, dong)
            encoded_dong = urllib.parse.quote(dong)
            dong_url = f"{BASE_URL}/region/{reg_key}/{dist_key}/{encoded_dong}/"
            urls.append(dong_url)
            
            full_dong_title = f"{reg_name} {dist_name} {dong}"
            p_title = f"{full_dong_title} 출장 {current_kw} 제휴업체 목록 | {BRAND_NAME}"
            m_desc = f"{full_dong_title} 출장 베스트 마사지 업체와 코스 정보를 누아결1004 에서 편리하게 확인하세요. 실시간 전화상담 {PHONE}"
            
            make_page(dong_dir, HTML_TEMPLATE.format(
                brand=BRAND_NAME, phone=PHONE, youtube_id=YOUTUBE_ID,
                map_query=urllib.parse.quote(full_dong_title),
                page_title=p_title,
                page_title_h1=f"{full_dong_title} 출장 {current_kw}",
                meta_description=m_desc,
                location_title=full_dong_title,
                canonical_url=dong_url,
                breadcrumbs=f'홈 › <a href="/region/{reg_key}/">{reg_name}</a> › <a href="/region/{reg_key}/{dist_key}/">{dist_name}</a> › {dong}',
                tag_section="",
                shop_cards_html=generate_shop_cards(full_dong_title)
            ))

# 4. sitemap.xml 생성
sitemap_xml = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for u in urls:
    sitemap_xml.append(f"  <url><loc>{u}</loc><priority>0.8</priority></url>")
sitemap_xml.append('</urlset>')

with open("sitemap.xml", "w", encoding="utf-8") as f:
    f.write("\n".join(sitemap_xml))

# 5. robots.txt 생성
with open("robots.txt", "w", encoding="utf-8") as f:
    f.write(f"User-agent: *\nAllow: /\n\nSitemap: {BASE_URL}/sitemap.xml\n")

print(f"완료! 누아결1004 총 {len(urls)}개의 다중 업체 상세 페이지 및 sitemap.xml, robots.txt 생성이 완료되었습니다.")