create table order_info
(
    id          char(32) not null
        constraint order_info_pk
            primary key,
    user_id     char(32)
        constraint order_info_user_info_id_fk
            references user_info,
    number      int,
    bucket_id   char(32)
        constraint order_info_flower_bucket_id_fk
            references flower_bucket,
    create_date datetime,
    status      int default 0
)
go

exec sp_addextendedproperty 'MS_Description', '用户购买记录', 'SCHEMA', 'dbo', 'TABLE', 'order_info'
go

exec sp_addextendedproperty 'MS_Description', '物理主键', 'SCHEMA', 'dbo', 'TABLE', 'order_info', 'COLUMN', 'id'
go

exec sp_addextendedproperty 'MS_Description', '用户id', 'SCHEMA', 'dbo', 'TABLE', 'order_info', 'COLUMN', 'user_id'
go

exec sp_addextendedproperty 'MS_Description', '购买数量', 'SCHEMA', 'dbo', 'TABLE', 'order_info', 'COLUMN', 'number'
go

exec sp_addextendedproperty 'MS_Description', '花卉id', 'SCHEMA', 'dbo', 'TABLE', 'order_info', 'COLUMN', 'bucket_id'
go

exec sp_addextendedproperty 'MS_Description', '订单时间', 'SCHEMA', 'dbo', 'TABLE', 'order_info', 'COLUMN', 'create_date'
go

create unique index order_info_id_uindex
    on order_info (id)
go

INSERT INTO flower.dbo.order_info (id, user_id, number, bucket_id, create_date, status) VALUES (N'1653311611906                   ', N'1653311611905                   ', 5, N'1653311611904                   ', N'2022-05-24 00:00:00.000', 3);
INSERT INTO flower.dbo.order_info (id, user_id, number, bucket_id, create_date, status) VALUES (N'1653311611907                   ', N'1653311611904                   ', 4, N'1653311611904                   ', N'2022-05-24 00:00:00.000', 0);
INSERT INTO flower.dbo.order_info (id, user_id, number, bucket_id, create_date, status) VALUES (N'1654198295360                   ', N'1654194864030                   ', 1, N'1654196181751                   ', N'2022-06-03 03:31:35.000', 0);
INSERT INTO flower.dbo.order_info (id, user_id, number, bucket_id, create_date, status) VALUES (N'1654198298999                   ', N'1654194864030                   ', 1, N'1654196181751                   ', N'2022-06-03 03:31:38.000', 0);
