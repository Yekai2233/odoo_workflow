# -*- coding: utf-8 -*-

from openerp import models, fields, api


class workflow_demo(models.Model):
    """
    Author  : SXY
    Date    : 2016/3/24 9:28
    Version : 1.0
    """
    _name = 'workflow_demo'

    WORKFLOW_STATE_SELECTION = [
        ('init', 'draft'),
        ('start', 'comfirm'),
        ('confirm', 'approve'),
        ('complete', 'complete'),
    ]

    name = fields.Char(string="name")
    text = fields.Text(string="todo")
    
    state = fields.Selection(WORKFLOW_STATE_SELECTION, default='init', string="status", readonly=True)
    user_id1 = fields.Many2one('res.users', string=u'确认人', default=lambda self:self.env.user)
    user_id2 = fields.Many2one('res.users', string=u'批准人', default=lambda self:self.env.user)
    

    # 注意使用新版本定义方法是，需要添加装饰器@api.one/@api.multi
    # 将state 置于开始状态
    @api.one
    def do_init(self):
        print("------------self.state = 'init'")
        self.state = 'init'
        return True

    @api.one
    def do_start(self):
        print("------------self.state = 'start'")
        self.state = 'start'
        return True

    # 将state 置于确认状态
    @api.one
    def do_confirm(self):
        print("------------self.state = 'confirm'")
        self.state = 'confirm'
        return True

    # 将state 置于完成状态
    @api.one
    def do_complete(self):
        print("------------self.state = 'complete'")
        self.state = 'complete'
        return True
