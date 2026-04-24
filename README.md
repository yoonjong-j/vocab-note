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

Vacabulary Notebook API는 단어를 저장하고 관리하며 학습할 수 있는 RESTful 백엔드 서비스입니다. 단어와 뜻, 예문을 등록하고, 랜덤으로 단어를 불러와 복습할 수 있습니다.

## 🛠 Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python 3.14.3 |
| Framework | FastAPI |
| Database | PostgreSQL |
| ORM | SQLAlchemy |
| Validation | Pydantic |
| Server | Uvicorn |

## 📋 Requirements

## Functional Requiements

| ID | Feature | Description | 설명 |
|----|---------|-------------|------|
| W-REQ-001 | Create Word | Add a new word with meaning and example | 단어, 뜻, 예문을 입력해서 새 단어 추가 |
| W-REQ-002 | Read All Words | Reatreive a list of all stored | 저장된 전체 단어 목록 조회 |
| W-REQ-003 | Read One Word | Retreive a single word by its ID | ID로 특정 단어 조회 |
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
http://localhost:8000
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

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yoonjong-j/vocab-note.git

cd vocab-note
```
## 📁 Project Structure
