#! python
import atexit, smtplib, ssl, os  
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.message import EmailMessage

class Gmail(object):
    def __init__(self, email:str, password:str, port:int=None, timeout:float=None, debugLevel:int=None):
        self.__state_key__ = 'state'
        self.__debug_level_key__ = 'debugLevel'
        self.__email_key__ = 'email'
        self.__password_key__ = 'password'
        self.__server_key__ = 'server'
        self.__port_key__ = 'port'
        self.__timeout_key__ = 'timeout'
        self.__context_key__ = 'context'
        self.__session_key__ = 'session'
        self.__exception_key__ = 'exception'
        self.__none_key__ = None
        self.__str_key__ = 'str'
        self.__int_key__ = 'int'
        self.__float_key__ = 'float'
        #port=465
        self.attribute_defaults = {
            self.__state_key__:[self.__str_key__, 'None'],
            self.__debug_level_key__:[self.__int_key__, 0],
            self.__email_key__:[self.__str_key__, None],
            self.__password_key__:[self.__str_key__, None],
            self.__server_key__:[self.__str_key__, 'smtp.gmail.com'],
            self.__port_key__:[self.__int_key__, 587],
            self.__timeout_key__:[self.__float_key__, 0.0],
            self.__context_key__:[self.__none_key__, ssl.create_default_context()],
            self.__session_key__:[self.__none_key__, None],
            self.__exception_key__:[self.__none_key__, None]}
        self.attributes = {}
        self.__set_state__('none')
        if debugLevel == None:  debugLevel = self.__get_attribute__(self.__debug_level_key__)
        else:  self.__set_attribute__(self.__debug_level_key__, int(debugLevel))
        self.__set_state__('initializing')
        self.__msg__(1, self.__get_state__())
        self.__set_attribute__(self.__email_key__, email)
        self.__set_attribute__(self.__password_key__, password)
        if port == None:  port = self.__get_attribute__(self.__port_key__)
        else:  self.__set_attribute__(self.__port_key__, int(port))
        if timeout == None:  timeout = self.__get_attribute__(self.__timeout_key__)
        else:  self.__set_attribute__(self.__timeout_key__, float(timeout))
        self.__set_state__('registering')
        atexit.register(self.close)
        self.__set_state__('initialized')
        try:
            self.__set_state__('creating')
            self.__msg__(1, self.__get_state__())
            if self.__get_attribute__(self.__timeout_key__) == 0.0:  self.__set_attribute__(self.__session_key__, smtplib.SMTP_SSL(self.__get_attribute__(self.__server_key__), self.__get_attribute__(self.__port_key__), context = self.__get_attribute__(self.__context_key__)))
            else:  self.__set_attribute__(self.__session_key__, smtplib.SMTP_SSL(self.__get_attribute__(self.__server_key__), self.__get_attribute__(self.__port_key__), context = self.__get_attribute__(self.__context_key__), timeout = self.__get_attribute__(self.__timeout_key__)))
            self.__set_state__('confirming create')
            self.__msg__(1, self.__get_state__())
            self.__get_attribute__(self.__session_key__).ehlo()
            self.__set_state__('created')
        except smtplib.SMTPServerDisconnected as ex:
            self.__set_state__('error')
            self.__set_attribute__(self.__exception_key__, ex)
            self.__msg__(0, f'create -- SMTPServerDisconnected: {self.__get_attribute__(self.__exception_key__)}')
        except smtplib.SMTPException as ex:
            self.__set_state__('error')
            self.__set_attribute__(self.__exception_key__, ex)
            self.__msg__(0, f'create -- SMTPException: {self.__get_attribute__(self.__exception_key__)}')
        except Exception as ex:
            self.__set_state__('error')
            self.__set_attribute__(self.__exception_key__, ex)
            self.__msg__(0, f'create -- Exception: {self.__get_attribute__(self.__exception_key__)}')
        finally:
            pass
        if self.__get_state__() == 'created':
            try:
                self.__set_state__('authenticating')
                self.__msg__(1, self.__get_state__())
                self.__get_attribute__(self.__session_key__).login(self.__get_attribute__(self.__email_key__), self.__get_attribute__(self.__password_key__))
                self.__set_state__('confirming authentication')
                self.__msg__(1, self.__get_state__())
                self.__get_attribute__(self.__session_key__).ehlo()
                self.__set_state__('authenticated')
                self.__msg__(1, self.__get_state__())
            except smtplib.SMTPServerDisconnected as ex:
                self.__set_state__('error')
                self.__set_attribute__(self.__exception_key__, ex)
                self.__msg__(0, f'{self.__get_attribute__(self.__state_key__)} -- SMTPServerDisconnected: {self.__get_attribute__(self.__exception_key__)}')
                if self.__get_attribute__(self.__session_key__) != None:  self.__get_attribute__(self.__session_key__).close()
            except smtplib.SMTPException as ex:
                self.__set_state__('error')
                self.__set_attribute__(self.__exception_key__, ex)
                self.__msg__(0, f'{self.__get_attribute__(self.__state_key__)} -- SMTPException: {self.__get_attribute__(self.__exception_key__)}')
                if self.__get_attribute__(self.__session_key__) != None:  self.__get_attribute__(self.__session_key__).close()
            except Exception as ex:
                self.__set_state__('error')
                self.__set_attribute__(self.__exception_key__, ex)
                self.__msg__(0, f'{self.__get_attribute__(self.__state_key__)} -- Exception: {self.__get_attribute__(self.__exception_key__)}')
                if self.__get_attribute__(self.__session_key__) != None:  self.__get_attribute__(self.__session_key__).close()
            finally:
                if self.__get_state__() == 'authenticated':  self.__msg__(1, 'created!')
                else:  self.__msg__(1, 'error creating!')

    def __msg__(self, level:int, msg=str):
        if self.__get_attribute__(self.__debug_level_key__) >= int(level): print(msg)

    def __state_msg__(self, level:int):
        self.__msg__(int(level), f'state:  {f"{self.__get_state__()}"}')

    def __set_state__(self, state:str):
        self.__set_attribute__(self.__state_key__, state, False)
        self.__state_msg__(3)

    def __get_state__(self):
        return self.__get_attribute__(self.__state_key__)

    def __set_attribute__(self, attribute:str, value, debug_msg=True):
        match self.attribute_defaults[attribute][0]:
            case self.__none_key__:
                pass
            case self.__str_key__:
                value = str(value)
            case self.__int_key__:
                value = int(value)
            case self.__float_key__:
                value = float(value)
        self.attributes[attribute] = value
        if debug_msg:  self.__msg__(2, f'{attribute}:  {self.__get_attribute__(attribute)}')

    def __get_attribute__(self, attribute:str, default_value=None):
        if default_value == None:  default_value = self.attribute_defaults[attribute][1]
        match self.attribute_defaults[attribute][0]:
            case self.__none_key__:
                pass
            case self.__str_key__:
                default_value = str(default_value)
            case self.__int_key__:
                default_value = int(default_value)
            case self.__float_key__:
                default_value = float(default_value)
        if attribute in self.attributes.keys():  return self.attributes[attribute]
        else:  self.__set_attribute__(attribute, default_value)
        return self.__get_attribute__(attribute)

    def close(self):
        if self.__get_state__() != 'closed':
            self.__msg__(1, 'Running cleanup...')
            if self.__get_attribute__(self.__session_key__) != None:  self.__get_attribute__(self.__session_key__).close()
            self.__set_state__('closed')
            self.__msg__(1, 'cleanup complete!')
        else:
            self.__msg__(3, 'already closed!')

    def send_message(self, to, subject, body, attach=None, fromEMail=None):
        if fromEMail == None:  fromEMail = self.__get_attribute__(self.__email_key__)
        if to == None:  to = self.__get_attribute__(self.__email_key__)
        msg = MIMEMultipart()
        msg['From'] = fromEMail
        msg['Subject'] = subject
        msg['To'] = to
        msg['MIME-Version'] = '1.0'
        msg['Content-Type'] = 'text/html'
        msg.attach(MIMEText(body))
        if attach != None:
            part = MIMEBase('application', 'octet-stream')
            try:
                part.set_payload(open(attach, 'rb').read())
            except Exception as ex:
                print(f"Error: {ex.args} {os.getcwd()}")
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(attach))
            msg.attach(part)

        #headers = [
        #    "From: " + fromEMail,
        #    "Subject: " + subject,
        #    "To: " + to,
        #    "MIME-Version: 1.0",
        #   "Content-Type: text/html"]
        #headers = "\r\n".join(headers)
        if self.__get_state__() == 'authenticated':
            self.__msg__(3, self.__get_attribute__(self.__email_key__))
            self.__msg__(3, f'to:  {to}')
            self.__msg__(3, f'from:  {fromEMail}')
            self.__msg__(3, f'subject:  {subject}')
            self.__msg__(3, f'body:  {body}')
            self.__msg__(3, f'msg:  {msg}')
            self.session.sendmail(
                from_addr = fromEMail,
                to_addrs = to,
#                headers + "\r\n\r\n" + body)
                msg = msg)
            self.__msg__(1, 'send complete!')
        else:
            self.__msg__(1, 'gmail not authenticated!')

username = "tmannathp@gmail.com"
passwd = "opnwewrfvhrshwou"
receiver = "tracy.mann1@retailbusinessservices.com"

def mail(from_email, to, subject, text, attach=None):
    #attach="./index-en.html"
    #// get the feedback div element so we can do something with it.
    msg = MIMEMultipart()

    msg['From'] = from_email
    msg['To'] = to
    msg['Subject'] = subject

    msg.attach(MIMEText(text)) 
    if attach != None:
        part = MIMEBase('application', 'octet-stream')
        try:
            part.set_payload(open(attach, 'rb').read())
        except Exception as ex:
            print(f"Error: {ex.args} {os.getcwd()}")
        #Encoders.encode_base64(part)
        #part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(attach))
        #msg.attach(part)

    try:
        print(f"pre-all")
        #with SMTP(host="smtp.gmail.com:465", timeout=300) as smtp:
        #with SMTP(host="smtp.gmail.com:465") as smtp:
        with SMTP(host="smtp.gmail.com:587", timeout=250) as smtp:
            print(f"created")
            try:
                step = "ehlo 1"
                smtp.ehlo()
                print(f"{step}")
                step = "login"
                smtp.login(username, passwd)
                print(f"{step}")
                step = "ehlo 2"
                smtp.ehlo()
                print(f"{step}")
                step = "tls start"
                smtp.starttls()
                print(f"{step}")
                step = "ehlo 3"
                smtp.ehlo()
                print(f"{step}")
            except Exception as ex:
                ex.args
                print(f"{step} -- Error: {ex.args}")
            finally:
                print("closed")
                smtp.close()
                pass
    except Exception as ex:
        ex.args
        print(f"create -- Error: {ex.args}")

#gm = Gmail(username, passwd, port=465, timeout=250, debugLevel=2)
#gm0 = Gmail(username, passwd, debugLevel=2)
gm1 = Gmail(username, passwd, timeout=250, debugLevel=3)
#gm2 = Gmail(username, passwd, timeout=250)

#gm.send_message(None, 'Subject', 'Message')
#gm0.send_message(receiver, 'Subject', 'Message')
gm1.send_message(receiver, 'Subject', 'Message')
#gm2.send_message(receiver, 'Subject', 'Message')
