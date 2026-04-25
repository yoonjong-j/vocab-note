# 📖 Vocabulary Notebook API

> A simple and clean REST API for managing your personal vocabulary notebook.<br>
나만의 단어장을 관리하는 심플한 REST API입니다.

## 👤 Author

**Yoonjong Jang / 장윤종**

GitHub: [@yoonjong-j](https://github.com/yoonjong-j)

## 📌 Overview

### English

Vocabulary Notebook API is a RESTful backend service that allows users to store, manage, and review vocabulary words. Users can add words with definitions and example sentences, and retrieve random words for review sessions.

### Korean

Vocabulary Notebook API는 단어를 저장하고 관리하며 학습할 수 있는 RESTful 백엔드 서비스입니다. 단어와 뜻, 예문을 등록하고, 랜덤으로 단어를 불러와 복습할 수 있습니다.

## 🛠 Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python 3.14.3 |
| Framework | FastAPI |
| Database | PostgreSQL |
| ORM | SQLAlchemy |
| Validation | Pydantic |
| Server | Uvicorn |
| AI Assist | Gemini, Gemini CLI |

## 📋 Requirements

## Functional Requirements

| ID | Feature | Description | 설명 |
|----|---------|-------------|------|
| W-REQ-001 | Create Word | Add a new word with meaning and example | 단어, 뜻, 예문을 입력해서 새 단어 추가 |
| W-REQ-002 | Read All Words | Retrieve a list of all stored | 저장된 전체 단어 목록 조회 |
| W-REQ-003 | Read One Word | Retrieve a single word by its ID | ID로 특정 단어 조회 |
| W-REQ-004 | Update Word | Modify an existing word's data | 기존 단어의 정보 수정 |
| W-REQ-005 | Delete Word | Remove a word by its ID | ID로 특정 단어 삭제 |
| W-REQ-006 | Random Word | Retrieve a random word for review | 복습용 랜덤 단어 1개 조회 |

## 🗂 ERD

### Diagram

[![ERD](/docs/images/erd.png)](https://www.erdcloud.com/d/CftC77PeZXpYjukpb)

### Field Description

| Column | Type | Constraints | Description | 설명 |
|--------|------|-------------|-------------|------|
| `word_id` | SERIAL | PK, NOT NULL | Auto-increment primary key | 자동 증가 기본키 |
| `word` | VARCHAR(200) | NOT NULL | Vocabulary word | 단어 |
| `word_meaning` | VARCHAR(300) | NOT NULL | Definition of the word | 단어 뜻 |
| `word_example` | VARCHAR(500) | NULL | Example Sentence | 예문 |
| `created_at` | TIMESTAMP | NOT NULL, DEFAULT NOW() | Record word creation time | 단어 생성 시각 |
| `updated_at` | TIMESTAMP | NULL | Record word last updated time | 단어 최종 수정 시간 |

## 📋 API Specification

### Base URL

```text
http://127.0.0.1:8000
```

### Endpoints

| Method | Endpoint | Description | 설명 |
|--------|----------|-------------|------|
| `GET` | `/words` | Get all words | 전체 단어 목록 조회 |
| `GET` | `/words/{word_id}` | Get a word by ID | 특정 단어 조회 |
| `GET` | `/words/random` | Get random word | 랜덤 단어 조회 |
| `POST` | `/words` | Add a new word | 단어 추가 |
| `PATCH` | `/words/{word_id}` | Update a word | 단어 수정 |
| `DELETE` | `/words/{word_id}` | Delete a word | 단어 삭제 |

## 📁 Project Structure

### English

```
 vocab-note/
  ├── app/                      # Application source code
  │   ├── routers/              # API route modules
  │   │   ├── __init__.py
  │   │   └── words.py          # API endpoints for vocabulary management
  │   ├── __init__.py
  │   ├── config.py             # Global configuration and environment settings
  │   ├── database.py           # Database connection and session handling
  │   ├── main.py               # FastAPI application entry point
  │   ├── models.py             # SQLAlchemy ORM models (Database schema)
  │   └── schemas.py            # Pydantic models (Data validation & serialization)
  ├── docs/                     # Documentation and design assets
  │   └── images/               # Image resources 
  │       └── erd.png           # Entity Relationship Diagram (ERD)
  ├── .env                      # Environment variables (DB URL, Secrets, etc.)
  ├── .gitignore                # Files and directories to be ignored by Git
  └── README.md                 # Project overview and instructions
```

### Korean

```
  vocab-note/                   
  ├── app/                      # 애플리케이션 소스 코드
  │   ├── routers/              # API 경로(Route) 모듈 관리
  │   │   ├── __init__.py
  │   │   └── words.py          # 단어 관리 관련 API 엔드포인트
  │   ├── __init__.py
  │   ├── config.py             # 전역 설정 및 환경 변수 관리
  │   ├── database.py           # 데이터베이스 연결 및 세션 설정
  │   ├── main.py               # FastAPI 애플리케이션 진입점
  │   ├── models.py             # SQLAlchemy ORM 모델 (DB 테이블 정의)
  │   └── schemas.py            # Pydantic 모델 (데이터 검증 및 직렬화)
  ├── docs/                     # 문서 및 설계 자산
  │   └── images/               # 이미지 리소스
  │       └── erd.png           # 데이터베이스 ERD (설계도)
  ├── .env                      # 환경 변수 설정 파일 (DB URL 등)
  ├── .gitignore                # Git 버전 관리 제외 대상 설정
  └── README.md                 # 프로젝트 개요 및 가이드
```

## 🚀 Getting Started

### 1. Prerequisites

- Python 3.10 or higher

### 2. Installation

```bash
git clone https://github.com/yoonjong-j/vocab-note.git
```

```bash
cd vocab-note
```

```
# .env file
DATABASE_URL=postgresql://[username]:[password]@[host_name]:[port]/[database_name]
```

### 3. Install Dependencies

```bash
pip install fastapi "uvicorn[standard]" sqlalchemy python-dotenv pydantic-settings
```

### 4. Environment Configuration

```bash
# PostgreSQL
pip install psycopg2-binary
```

### 5. Running the Server

```bash
uvicorn app.main:app --reload
```

#### API Server

```
http://127.0.0.1:8000
```

#### Interactive Docs (Swagger UI)

```
http://127.0.0.1:8000/docs
```

## 📍 Future Roadmap (Backlog)

### 🎨 Frontend Development

- [ ] Build a web-based UI to interact with the API (API 연동 웹 UI 구축)
- [ ] Implement word search and quiz interfaces (단어 검색 및 퀴즈 인터페이스 구현)

### 🔐 User Authentication

- [ ] Implement Sign-up and Login functionality using JWT (JWT 기반 회원가입/로그인 구현)
- [ ] Add private vocabulary management for individual users (사용자별 개인 단어장 관리 기능 추가)
