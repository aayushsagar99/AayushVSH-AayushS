node{
stage('Email Notification'){
mail bcc: '', body: '''Build successful!!!!
Thanks,
Sagar''', cc: '', from: '', replyTo: '', subject: 'Build successfull', to: 'vs.sagar@gmail.com'
}
}
