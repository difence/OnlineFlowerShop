create table user_info
(
    id          char(32) not null
        constraint user_info_pk
            primary key,
    account     char(32) not null,
    password    char(128),
    tel         char(16),
    score       float,
    score_sum   float,
    birth       date,
    create_date datetime,
    update_date datetime,
    auth        int default 0
)
go

exec sp_addextendedproperty 'MS_Description', '用户信息表', 'SCHEMA', 'dbo', 'TABLE', 'user_info'
go

exec sp_addextendedproperty 'MS_Description', '物理主键', 'SCHEMA', 'dbo', 'TABLE', 'user_info', 'COLUMN', 'id'
go

exec sp_addextendedproperty 'MS_Description', '账号', 'SCHEMA', 'dbo', 'TABLE', 'user_info', 'COLUMN', 'account'
go

exec sp_addextendedproperty 'MS_Description', '密码', 'SCHEMA', 'dbo', 'TABLE', 'user_info', 'COLUMN', 'password'
go

exec sp_addextendedproperty 'MS_Description', '电话', 'SCHEMA', 'dbo', 'TABLE', 'user_info', 'COLUMN', 'tel'
go

exec sp_addextendedproperty 'MS_Description', '积分', 'SCHEMA', 'dbo', 'TABLE', 'user_info', 'COLUMN', 'score'
go

exec sp_addextendedproperty 'MS_Description', '总积分', 'SCHEMA', 'dbo', 'TABLE', 'user_info', 'COLUMN', 'score_sum'
go

exec sp_addextendedproperty 'MS_Description', '出生日期', 'SCHEMA', 'dbo', 'TABLE', 'user_info', 'COLUMN', 'birth'
go

exec sp_addextendedproperty 'MS_Description', '创建时间', 'SCHEMA', 'dbo', 'TABLE', 'user_info', 'COLUMN', 'create_date'
go

exec sp_addextendedproperty 'MS_Description', '更新时间', 'SCHEMA', 'dbo', 'TABLE', 'user_info', 'COLUMN', 'update_date'
go

create unique index user_info_id_uindex
    on user_info (id)
go

create unique index user_info_account_uindex
    on user_info (account)
go

INSERT INTO flower.dbo.user_info (id, account, password, tel, score, score_sum, birth, create_date, update_date, auth) VALUES (N'1653311611904                   ', N'ssj                             ', N'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3                                                                ', N'123             ', 0, 0, N'2002-01-01', N'2022-05-24 00:00:00.000', N'2022-05-24 00:00:00.000', null);
INSERT INTO flower.dbo.user_info (id, account, password, tel, score, score_sum, birth, create_date, update_date, auth) VALUES (N'1653311611905                   ', N'admin                           ', N'8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918                                                                ', N'123456          ', 0, 0, N'2022-05-06', N'2022-05-23 00:00:00.000', N'2022-05-23 00:00:00.000', 1);
INSERT INTO flower.dbo.user_info (id, account, password, tel, score, score_sum, birth, create_date, update_date, auth) VALUES (N'1654194864030                   ', N'ss                              ', N'6b51d431df5d7f141cbececcf79edf3dd861c3b4069f0b11661a3eefacbba918                                                                ', N'123             ', 0, 0, N'2002-05-06', N'2022-06-03 02:34:24.000', N'2022-06-03 02:34:24.000', 0);
INSERT INTO flower.dbo.user_info (id, account, password, tel, score, score_sum, birth, create_date, update_date, auth) VALUES (N'1654194895951                   ', N'123                             ', N'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3                                                                ', N'123             ', 0, 0, N'2002-05-06', N'2022-06-03 02:34:55.000', N'2022-06-03 02:34:55.000', 0);
INSERT INTO flower.dbo.user_info (id, account, password, tel, score, score_sum, birth, create_date, update_date, auth) VALUES (N'1654194903673                   ', N'qaz                             ', N'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3                                                                ', N'123             ', 0, 0, N'2002-05-06', N'2022-06-03 02:35:03.000', N'2022-06-03 02:35:03.000', 0);
