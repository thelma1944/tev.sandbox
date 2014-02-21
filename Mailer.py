class Mailer()
{

    MailMessage ms;
    SmtpClient Sc;
    public Mailer()
    {
        Sc = new SmtpClient("smtp.gmail.com");

        //Sc.Credentials = CredentialCache.DefaultNetworkCredentials;
        Sc.EnableSsl = true;
        Sc.Port =465;
        Sc.Timeout = 900000000;
        Sc.DeliveryMethod = SmtpDeliveryMethod.Network;
        Sc.UseDefaultCredentials = false;
        Sc.Credentials = new NetworkCredential("uid", "mypss");


    }
    public void MailTodaysBirthdays(List<Celebrant> TodaysCelebrant)
    {
        int i = TodaysCelebrant.Count();
        foreach (Celebrant cs in TodaysCelebrant)
        {
            //if (IsEmail(cs.EmailAddress.ToString().Trim()))
            //{
           ms = new MailMessage();
           ms.To.Add(cs.EmailAddress);
           ms.From = new MailAddress("uid","Developers",System.Text.Encoding.UTF8);
           ms.Subject = "Happy Birthday ";

           String EmailBody = "Happy Birthday " + cs.FirstName;
           ms.Body = EmailBody;
           ms.Priority = MailPriority.High;

           try
            {
              Sc.Send(ms);
            }
                catch (Exception ex)
                {
                    Sc.Send(ms);
                    BirthdayServices.LogEvent(ex.Message.ToString(),EventLogEntryType.Error);
                }
            //}


        }

    }


    }