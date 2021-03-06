# model settings
norm_cfg = dict(type='SyncBN', requires_grad=True)
model = dict(
    type='EncoderDecoder',
    pretrained='/shared/xudongliu/models/dla34-24a49e58.pth',
    backbone=dict(
        type='DLA',
        levels=[1, 1, 1, 2, 2, 1],
        channels=[16, 32, 64, 128, 256, 512],
        block_num=2,
        num_classes=19,
        return_levels=True,
        norm_cfg=norm_cfg
        ),
    neck=dict(
        type='DLAUp',
        channels=[32, 64, 128, 256, 512],
        scales=(1, 2, 4, 8, 16),
        norm_cfg=norm_cfg
        ),
    decode_head=dict(
            type='DLAsHead',
            channels=32,
            in_channels=32,
            num_classes=3,
            dropout_ratio=0,
            ignore_index=255,
            loss_decode=dict(
                     type='CrossEntropyLoss',
                     use_sigmoid=False,
                     loss_weight=1.0),
            )
    )
# model training and testing settings
train_cfg = dict()
test_cfg = dict(mode='whole')
