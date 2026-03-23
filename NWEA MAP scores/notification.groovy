node{
stage('Email Notification'){
mail bcc: '', body: '''Build successful!!!!
Thanks,
Sagar''', cc: '', from: aayushsagar99@gmail.com'', replyTo: '', subject: 'Build successfull', to: 'vs.sagar@gmail.com'
}
}
