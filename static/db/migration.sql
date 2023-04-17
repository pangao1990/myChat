CREATE TABLE alembic_version (
    version_num VARCHAR(32) NOT NULL,
    CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
);
-- Running upgrade  -> f315a762b0fe
CREATE TABLE storage_var (
    id INTEGER NOT NULL,
    "key" VARCHAR NOT NULL,
    value VARCHAR DEFAULT '' NOT NULL,
    created_at DATETIME DEFAULT (DATETIME(CURRENT_TIMESTAMP, 'localtime')),
    updated_at DATETIME DEFAULT (DATETIME(CURRENT_TIMESTAMP, 'localtime')),
    PRIMARY KEY (id)
);
CREATE INDEX ix_storage_var_key ON storage_var ("key");
INSERT INTO alembic_version (version_num)
VALUES ('f315a762b0fe')
RETURNING version_num;
-- Running upgrade f315a762b0fe -> 86c3f491c4cc
ALTER TABLE storage_var
ADD COLUMN remark VARCHAR DEFAULT '' NOT NULL;
UPDATE alembic_version
SET version_num = '86c3f491c4cc'
WHERE alembic_version.version_num = 'f315a762b0fe';
-- Running upgrade 86c3f491c4cc -> 826223a88f2b
CREATE TABLE chat (
    id INTEGER NOT NULL,
    title INTEGER DEFAULT '' NOT NULL,
    who VARCHAR DEFAULT '' NOT NULL,
    content VARCHAR DEFAULT '' NOT NULL,
    created_at DATETIME DEFAULT (DATETIME(CURRENT_TIMESTAMP, 'localtime')),
    updated_at DATETIME DEFAULT (DATETIME(CURRENT_TIMESTAMP, 'localtime')),
    PRIMARY KEY (id)
);
CREATE INDEX ix_chat_title ON chat (title);
CREATE TABLE title (
    id INTEGER NOT NULL,
    title VARCHAR DEFAULT '' NOT NULL,
    theme VARCHAR DEFAULT '' NOT NULL,
    model VARCHAR DEFAULT 'gpt-3.5-turbo' NOT NULL,
    temperature FLOAT DEFAULT '1.0' NOT NULL,
    news_count INTEGER DEFAULT '0' NOT NULL,
    created_at DATETIME DEFAULT (DATETIME(CURRENT_TIMESTAMP, 'localtime')),
    updated_at DATETIME DEFAULT (DATETIME(CURRENT_TIMESTAMP, 'localtime')),
    PRIMARY KEY (id)
);
CREATE INDEX ix_title_title ON title (title);
UPDATE alembic_version
SET version_num = '826223a88f2b'
WHERE alembic_version.version_num = '86c3f491c4cc';