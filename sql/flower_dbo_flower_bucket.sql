create table flower_bucket
(
    id             char(32) not null
        constraint flower_bucket_pk
            primary key,
    name           nvarchar(32),
    color          nvarchar(32),
    offer_id       char(32)
        constraint flower_bucket_offer_info_id_fk
            references offer_info,
    bucket         int default 0,
    msg            nvarchar(128),
    due_date       date,
    price          float,
    attachment_ids char(128),
    create_date    datetime,
    update_date    datetime
)
go

exec sp_addextendedproperty 'MS_Description', '花卉库存', 'SCHEMA', 'dbo', 'TABLE', 'flower_bucket'
go

exec sp_addextendedproperty 'MS_Description', '物理主键', 'SCHEMA', 'dbo', 'TABLE', 'flower_bucket', 'COLUMN', 'id'
go

exec sp_addextendedproperty 'MS_Description', '花卉名字', 'SCHEMA', 'dbo', 'TABLE', 'flower_bucket', 'COLUMN', 'name'
go

exec sp_addextendedproperty 'MS_Description', '花卉颜色', 'SCHEMA', 'dbo', 'TABLE', 'flower_bucket', 'COLUMN', 'color'
go

exec sp_addextendedproperty 'MS_Description', '供应商id', 'SCHEMA', 'dbo', 'TABLE', 'flower_bucket', 'COLUMN', 'offer_id'
go

exec sp_addextendedproperty 'MS_Description', '库存数量', 'SCHEMA', 'dbo', 'TABLE', 'flower_bucket', 'COLUMN', 'bucket'
go

exec sp_addextendedproperty 'MS_Description', '备注', 'SCHEMA', 'dbo', 'TABLE', 'flower_bucket', 'COLUMN', 'msg'
go

exec sp_addextendedproperty 'MS_Description', '过期时间', 'SCHEMA', 'dbo', 'TABLE', 'flower_bucket', 'COLUMN', 'due_date'
go

exec sp_addextendedproperty 'MS_Description', '价格', 'SCHEMA', 'dbo', 'TABLE', 'flower_bucket', 'COLUMN', 'price'
go

exec sp_addextendedproperty 'MS_Description', '更新时间', 'SCHEMA', 'dbo', 'TABLE', 'flower_bucket', 'COLUMN', 'create_date'
go

exec sp_addextendedproperty 'MS_Description', '创建时间', 'SCHEMA', 'dbo', 'TABLE', 'flower_bucket', 'COLUMN', 'update_date'
go

create unique index flower_bucket_id_uindex
    on flower_bucket (id)
go

INSERT INTO flower.dbo.flower_bucket (id, name, color, offer_id, bucket, msg, due_date, price, attachment_ids, create_date, update_date) VALUES (N'1653311611904                   ', N'菊花', N'黄色', N'1653311611903                   ', 11, N'无', N'2022-05-31', 10, N'1653311611903                                                                                                                   ', N'2022-05-24 00:00:00.000', N'2022-05-17 00:00:00.000');
INSERT INTO flower.dbo.flower_bucket (id, name, color, offer_id, bucket, msg, due_date, price, attachment_ids, create_date, update_date) VALUES (N'1654196181751                   ', N'水仙', N'蓝色', N'1653311611903                   ', 2, N'无', N'2022-07-03', 128, N'                                                                                                                                ', N'2022-06-03 02:56:21.000', N'2022-06-03 02:56:21.000');
