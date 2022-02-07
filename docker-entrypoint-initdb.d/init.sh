set -e
psql -U ${POSTGRES_USER} -d ${POSTGRES_DB}<< EOSQL
CREATE TABLE users ( id serial, mail varchar(256) NOT NULL UNIQUE, password varchar(64) NOT NULL, salt varchar(64) NOT NULL, name varchar(64) NOT NULL, is_newuser boolean NOT NULL, user_type smallint NOT NULL, created_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP , updated_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP , PRIMARY KEY (id));

CREATE TABLE departments ( id smallserial, name varchar(30) NOT NULL, is_show boolean NOT NULL DEFAULT true, PRIMARY KEY (id));

CREATE TABLE students ( id integer, graduation_year smallint NOT NULL, student_number integer NOT NULL, department_id smallint, teacher_id integer, PRIMARY KEY (id), FOREIGN KEY (id) REFERENCES users(id), FOREIGN KEY (department_id) REFERENCES departments(id), FOREIGN KEY (teacher_id) REFERENCES users(id));

CREATE TABLE change_passwords ( id smallserial, user_id integer NOT NULL, hash varchar(64) NOT NULL, is_changed boolean NOT NULL DEFAULT false, exp_datetime timestamp NOT NULL, created_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP , updated_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP, PRIMARY KEY (id), FOREIGN KEY (user_id) REFERENCES users(id));

CREATE TABLE web_push ( id serial, user_id integer NOT NULL, public_key varchar(255) NOT NULL, endpoint varchar(2048) NOT NULL, secret_key varchar(255) NOT NULL, PRIMARY KEY (id), FOREIGN KEY (user_id)REFERENCES users(id));

CREATE TABLE industries ( id smallserial, name varchar(64) NOT NULL, is_show boolean NOT NULL DEFAULT true, PRIMARY KEY (id));

CREATE TABLE occupations ( id smallserial, name varchar(64) NOT NULL, is_show boolean NOT NULL DEFAULT true, industry_id smallint NOT NULL, PRIMARY KEY (id), FOREIGN KEY (industry_id)REFERENCES industries(id));

CREATE TABLE reports ( id serial, student_id integer NOT NULL, teacher_id integer NOT NULL, company varchar(256) NOT NULL, zip_code varchar(7) NOT NULL, prefecture varchar(4) NOT NULL, address varchar(256) NOT NULL, occupations_id smallint NOT NULL, form varchar(16) NOT NULL, advice varchar(1024), is_show boolean NOT NULL DEFAULT true, job_teacher_id integer, test_result smallint NOT NULL, created_at timestamp NOT NULL  DEFAULT CURRENT_TIMESTAMP, updated_at timestamp NOT NULL  DEFAULT CURRENT_TIMESTAMP, PRIMARY KEY (id), FOREIGN KEY (student_id) REFERENCES users(id), FOREIGN KEY (teacher_id) REFERENCES users(id), FOREIGN KEY (job_teacher_id) REFERENCES users(id), FOREIGN KEY (occupations_id) REFERENCES occupations(id));

CREATE TABLE tests ( id serial, report_id integer, stage smallint NOT NULL, start_date timestamp NOT NULL, end_date timestamp NOT NULL, datails_text varchar(1024), is_status smallint NOT NULL, is_checked_student boolean NOT NULL, created_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP, updated_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP, PRIMARY KEY (id), FOREIGN KEY (report_id)REFERENCES reports(id));

CREATE TABLE test_details( test_id integer, detail_id serial, test_category smallint NOT NULL, data1 varchar(32), data2 varchar(32), created_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP, updated_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP, PRIMARY KEY (test_id, detail_id), FOREIGN KEY (test_id) REFERENCES tests(id));

CREATE TABLE test_report_reviews ( review_id serial, test_id integer, comment varchar(1024) NOT NULL, created_at timestamp NOT NULL  DEFAULT CURRENT_TIMESTAMP, updated_at timestamp NOT NULL  DEFAULT CURRENT_TIMESTAMP, PRIMARY KEY (review_id, test_id), FOREIGN KEY (test_id) REFERENCES tests(id));

INSERT INTO users (mail, password, salt, name, is_newuser, user_type) VALUES ('kenta.sato.sys19@morijyobi.ac.jp', '457df00d3277f8f28479f18b5754359c794224e217acfd60da9f09cb6b94e344', 'rgOOGAJqKQypkSnQchCfehaNjicvbqOLlLiULBmaURYyCWsZaBNVgENRAzNUbqoX', '佐藤健太', false, '0');
INSERT INTO users (mail, password, salt, name, is_newuser, user_type) VALUES ('t.hanasaka.sys20@morijyobi.ac.jp', 'c980e1dbac7a15ba0bacd647413f6ea33e6a55b8d79b8694332904ad0e110b1d', 'eSrtezZEAmKdDosoLfMkXHvtvuGRJslXTnuZrcxhuwIyqiDBBMrPuRRLeZVuSBXX', '斎藤次郎', false, '0');
INSERT INTO users (mail, password, salt, name, is_newuser, user_type) VALUES ('tarou.fugoukaku.sys21@morijyobi.ac.jp', '05a7512223fbcdd7a1e973ccac4a03181c79c4563881ce12479432ae88e4eec1', 'vsOQrbIgzhFsMrEEZQiYsbIOYZNWCnsusZARlqjXvTGlzsAdJCRiseodQPpYcRMs', '不太郎', true, '0');
INSERT INTO users (mail, password, salt, name, is_newuser, user_type) VALUES ('ootubo.kyoin@morijyobi.ac.jp', 'cf8edd141bb715a324b70e06634363712a3d160364b3bbb9e5f0420d0bfadff8', 'ZeUxiuYXGbyYgdWtqUjmwBwglwBKGhOcUMyhPyRFaAjcotKnJBOutgwCjlFUIjes', '大坪直行', false, '1');
INSERT INTO users (mail, password, salt, name, is_newuser, user_type) VALUES ('takahashi.kyoin@morijyobi.ac.jp', '89f7b216a3c90c159b4dff063f464650edd160b61d12b58094ceb015e09a8881', 'DCxomMyVeXdqIHkUCNSzRQcWqBUotxAWYIiXCkkbIJiZojObQZIKXjEyXzBXOvaK', '高橋一', false, '1');
INSERT INTO users (mail, password, salt, name, is_newuser, user_type) VALUES ('oikawa.syusyoku@morijyobi.ac.jp', '9d64abfc4822a0e66cd66c984774ec28f0b6151e5140bcbe299df014e17fd595', 'DTyZZfhgRFdOMDxKogRPPVuwBwRjdRUOJgUisisqqxsaVWBryeSWfmWesrZdDBZl', '及川高', false, '2');
INSERT INTO departments (name) VALUES ('高度情報工学科');
INSERT INTO departments (name) VALUES ('情報ビジネス科会計事務コース');
INSERT INTO departments (name) VALUES ('総合デザイン科デザインコース');
INSERT INTO departments (name, is_show) VALUES ('総合体育科ビジネス実習コース', false);
INSERT INTO students (id, graduation_year, student_number, department_id, teacher_id) VALUES (1, '2023', 4194102, 1, 4);
INSERT INTO students (id, graduation_year, student_number, department_id, teacher_id) VALUES (2, '2022', 3203101, 2, 5);
INSERT INTO students (id, graduation_year, student_number, department_id, teacher_id) VALUES (3, '2024', 2212101, 3, 5);
INSERT INTO industries (name) VALUES ('情報通信業');
INSERT INTO industries (name) VALUES ('建設業');
INSERT INTO industries (name) VALUES ('サービス業');
INSERT INTO industries (name) VALUES ('卸売業');
INSERT INTO industries (name) VALUES ('製造業');
INSERT INTO occupations (name, industry_id) VALUES ('システムエンジニア', 1);
INSERT INTO occupations (name, industry_id) VALUES ('Webエンジニア', 1);
INSERT INTO occupations (name, industry_id) VALUES ('家具デザイナー', 2);
INSERT INTO occupations (name, industry_id) VALUES ('調理師', 3);
INSERT INTO occupations (name, industry_id) VALUES ('スーパー', 4);
INSERT INTO occupations (name, industry_id) VALUES ('工場', 5);
INSERT INTO reports (student_id, teacher_id, company, zip_code, prefecture, address, occupations_id, form, advice, is_show, job_teacher_id, test_result) VALUES (1, 4, '株式会社aaa', '0200107', '岩手県', '岩手県盛岡市松園区松内町3丁目', 1, '自己開拓', '試験自体は難しいものではないので一つ一つ丁寧に行きましょう', false, null, 0);
INSERT INTO reports (student_id, teacher_id, company, zip_code, prefecture, address, occupations_id, form, advice, is_show, job_teacher_id, test_result) VALUES (2, 4, '株式会社bbb', '1600004', '東京都', '東京都新宿区四谷２丁目', 2, '縁故', 'インターンには参加したほうがいいです、気に入られれば人事と仲良くなれます', true, null, 1);
INSERT INTO reports (student_id, teacher_id, company, zip_code, prefecture, address, occupations_id, form, advice, is_show, job_teacher_id, test_result) VALUES (3, 5, '株式会社ccc', '9040004', '沖縄県', '沖縄県沖縄市中央２丁目１', 3, '学校', 'SPI対策はしっかりしておきましょう、本番の問題は大学レベルのものまで出ます。', true, 6, 2);
INSERT INTO reports (student_id, teacher_id, company, zip_code, prefecture, address, occupations_id, form, advice, is_show, job_teacher_id, test_result) VALUES (1, 4, '株式会社ddd', '0984451', '北海道', '北海道天塩郡豊富町', 4, '学校', '人間性がよく見られます。ベンチャー企業で、イケイケの人たちの集まりなので性格が合えばきっと働きやすい企業なんだと思います', true, 6, 3);
INSERT INTO reports (student_id, teacher_id, company, zip_code, prefecture, address, occupations_id, form, advice, is_show, job_teacher_id, test_result) VALUES (2, 5, '株式会社eee', '8701223', '大分県', ' 大分県大分市今市1882-1', 5, '学校', '試験自体もその人がどのような人か判断するだけのようなものなので受験すれば内定を貰えると思います', true, 6, 4);
INSERT INTO tests (report_id, stage, start_date, end_date, datails_text, is_status, is_checked_student) VALUES (1, 1, '2022-01-01 10:00:00', '2022-01-01 12:00:00', '受験者は私一人に対して面接官は3人いました。・なぜモリジョビを選んだか・なぜ自社なのか・自分は思う自社を代表する製品はなにか・自己PR以外の自分が他より勝る部分は何か・希望は営業だけか・志望した動機はなにか・3年後、自分はどうなっていると思うか。作文は「人生においての仕事のありかたとは」という題材で制限時間はそこまで長くないです。SPIも普段の対策をしていれば落とすことはないです。', 2, true);
INSERT INTO tests (report_id, stage, start_date, end_date, datails_text, is_status, is_checked_student) VALUES (2, 1, '2022-01-14 15:00:00', '2022-01-14 15:30:00', '面接官と以前からのやり取りでほぼ内定は確実だったので、会社概要など情報の共有程度で試験は終わりました。', 1, false);
INSERT INTO tests (report_id, stage, start_date, end_date, datails_text, is_status, is_checked_student) VALUES (3, 1, '2022-10-13 12:00:00', '2022-10-13 14:00:00', 'SPIは時間が限られていて余裕は少なかったです。問題自体もとても難しいもので、対策をしっかりとたてて本番では焦らないことが大事です。', 3, true);
INSERT INTO tests (report_id, stage, start_date, end_date, datails_text, is_status, is_checked_student) VALUES (3, 2, '2022-11-11 11:00:00', '2022-11-11 13:00:00', '面接は私一人に対して、役員や会長を含めて5人の面接官でした。答えるたびにメモなどを取られるので不安や焦りが募るもので、物々しい雰囲気でした。', 3, false);
INSERT INTO tests (report_id, stage, start_date, end_date, datails_text, is_status, is_checked_student) VALUES (4, 1, '2022-01-02 9:00:00', '2022-01-02 9:30:00', 'SPIも作文もただ受けるだけでいい簡単なものでした。面接自体もとてもラフなものでしたが社長さんも部長さんも若くてとても元気な方なので私とは少し価値観などが共感できなかったです。', 0, false);
INSERT INTO tests (report_id, stage, start_date, end_date, datails_text, is_status, is_checked_student) VALUES (5, 1, '2022-01-14 15:00:00', '2022-01-14 15:30:00', '面接のみの試験で正直人が足りていないので受験すれば合格できます。', 1, false);
INSERT INTO test_details (test_id, test_category, data1, data2) VALUES (1, 2, null, null);
INSERT INTO test_details (test_id, test_category, data1, data2) VALUES (1, 4, null, null);
INSERT INTO test_details (test_id, test_category, data1, data2) VALUES (1, 6, '3', '60');
INSERT INTO test_details (test_id, test_category, data1, data2) VALUES (2, 6, '1', '30');
INSERT INTO test_details (test_id, test_category, data1, data2) VALUES (3, 2, null, null);
INSERT INTO test_details (test_id, test_category, data1, data2) VALUES (4, 6, '5', '120');
INSERT INTO test_details (test_id, test_category, data1, data2) VALUES (5, 6, '2', '0');
INSERT INTO test_details (test_id, test_category, data1, data2) VALUES (6, 6, '1', '30');
INSERT INTO test_report_reviews (test_id, comment) VALUES (1, 'もう少し内容を詳しく記述してください');
INSERT INTO test_report_reviews (test_id, comment) VALUES (3, '承認します、2次試験も頑張ってください');
INSERT INTO test_report_reviews (test_id, comment) VALUES (4, 'お疲れ様でした、今回は残念な結果になりましたが次も頑張ってください');
EOSQL
