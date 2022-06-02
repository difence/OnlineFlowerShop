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
    update_date date
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

INSERT INTO flower.dbo.file_info (id, name, type, tname, update_id, update_date) VALUES (N'1653311611903                   ', N'1', N'2', N'3', N'1653311611905                   ', N'2022-05-24');
