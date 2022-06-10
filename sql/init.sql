create table offer_info
(
    id             char(32)     not null
        constraint offer_info_pk
            primary key,
    name           nvarchar(32) not null,
    msg            nvarchar(128),
    attachment_ids nvarchar(128),
    create_date    datetime,
    update_date    datetime
)
go

exec sp_addextendedproperty 'MS_Description', '供应商信息', 'SCHEMA', 'dbo', 'TABLE', 'offer_info'
go

exec sp_addextendedproperty 'MS_Description', '物理主键', 'SCHEMA', 'dbo', 'TABLE', 'offer_info', 'COLUMN', 'id'
go

exec sp_addextendedproperty 'MS_Description', '供应商名称', 'SCHEMA', 'dbo', 'TABLE', 'offer_info', 'COLUMN', 'name'
go

exec sp_addextendedproperty 'MS_Description', '供应商备注', 'SCHEMA', 'dbo', 'TABLE', 'offer_info', 'COLUMN', 'msg'
go

exec sp_addextendedproperty 'MS_Description', '附件id表', 'SCHEMA', 'dbo', 'TABLE', 'offer_info', 'COLUMN',
     'attachment_ids'
go

exec sp_addextendedproperty 'MS_Description', '创建时间', 'SCHEMA', 'dbo', 'TABLE', 'offer_info', 'COLUMN', 'create_date'
go

exec sp_addextendedproperty 'MS_Description', '更新时间', 'SCHEMA', 'dbo', 'TABLE', 'offer_info', 'COLUMN', 'update_date'
go

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

create trigger delete_flower_bucket
on flower_bucket
for delete
as
update sys_info set flower_bucket = flower_bucket - 1
go

create trigger insert_flower_bucket
on flower_bucket
for insert
as
update sys_info set flower_bucket = flower_bucket + 1
go

create unique index offer_info_id_uindex
    on offer_info (id)
go

create unique index offer_info_name_uindex
    on offer_info (name)
go

create trigger delete_offer_info
on offer_info
for delete
as
update sys_info set offer_info = offer_info - 1
go

create trigger insert_offer_info
on offer_info
for insert
as
update sys_info set offer_info = offer_info + 1
go

create table sys_info
(
    flower_bucket int,
    offer_info    int,
    order_info    int,
    user_info     int,
    file_info     int
)
go

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

create table file_info
(
    id          char(32) not null
        constraint file_info_pk
            primary key,
    name        varchar(32),
    type        varchar(16),
    tname       varchar(32),
    update_id   char(32)
        constraint file_info_user_info_id_fk
            references user_info,
    update_date datetime
)
go

exec sp_addextendedproperty 'MS_Description', '文件信息', 'SCHEMA', 'dbo', 'TABLE', 'file_info'
go

exec sp_addextendedproperty 'MS_Description', '物理主键', 'SCHEMA', 'dbo', 'TABLE', 'file_info', 'COLUMN', 'id'
go

exec sp_addextendedproperty 'MS_Description', '文件名称', 'SCHEMA', 'dbo', 'TABLE', 'file_info', 'COLUMN', 'name'
go

exec sp_addextendedproperty 'MS_Description', '文件后缀', 'SCHEMA', 'dbo', 'TABLE', 'file_info', 'COLUMN', 'type'
go

exec sp_addextendedproperty 'MS_Description', '文件全名', 'SCHEMA', 'dbo', 'TABLE', 'file_info', 'COLUMN', 'tname'
go

exec sp_addextendedproperty 'MS_Description', '上传用户', 'SCHEMA', 'dbo', 'TABLE', 'file_info', 'COLUMN', 'update_id'
go

exec sp_addextendedproperty 'MS_Description', '上传时间', 'SCHEMA', 'dbo', 'TABLE', 'file_info', 'COLUMN', 'update_date'
go

create unique index file_info_id_uindex
    on file_info (id)
go

create trigger delete_file_info
on file_info
for delete
as
update sys_info set file_info = file_info - 1
go

create trigger insert_file_info
on file_info
for insert
as
update sys_info set file_info = file_info + 1
go

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

create trigger delete_order_info
on order_info
for delete
as
update sys_info set order_info = order_info - 1
go

create trigger insert_order_info
on order_info
for insert
as
update sys_info set order_info = order_info + 1
go

create unique index user_info_id_uindex
    on user_info (id)
go

create unique index user_info_account_uindex
    on user_info (account)
go

create trigger delete_user_info
on user_info
for delete
as
update sys_info set user_info = user_info - 1
go

create trigger insert_user_info
on user_info
for insert
as
update sys_info set user_info = user_info + 1
go

create view file_VIEW as
    select *
    from file_info
go

create view flower_VIEW as
    select *
    from flower_bucket
go

create view flower_offer_VIEW as
    select offer_info.id as off_id,offer_info.name as offer_name,offer_info.msg,offer_info.attachment_ids,flower_bucket.id as flower_id,flower_bucket.name as flower_name,flower_bucket.color
    from flower_bucket,offer_info
    where flower_bucket.offer_id = offer_info.id
go

create view order_VIEW as
    select id,user_id,number,bucket_id,create_date,status
    from order_info
go

create view user_VIEW as
    select *
    from user_info
go

