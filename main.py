import logging

from apscheduler.schedulers.blocking import BlockingScheduler

from db import insert_balance
from zjzxdq import get_balance
from send_mail import send_mail
import config


logging.root.setLevel('INFO')

alert_number = config.ALERT_NUMBER
to_email = config.TO_MAIL


def job():
    balance = get_balance()
    logging.info(f'余额{balance}')
    insert_balance(balance)
    logging.info(f'写入数据库')
    if float(balance) < alert_number:
        content = f'余额仅剩: {balance}, 请尽快充值'
        send_mail(to_email, content, '电表余额提醒')


def main():
    logging.info('尝试查表一次')
    job()
    logging.info('尝试发送邮件一次')
    send_mail(to_email, '邮件功能完好!', '电表余额提醒服务启动测试')

    scheduler = BlockingScheduler(timezone='Asia/Shanghai')
    scheduler.add_job(job, 'cron', hour='*/6', id='balance')
    scheduler.start()


if __name__ == '__main__':
    main()
