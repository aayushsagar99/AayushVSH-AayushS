node{
stage('Email Notification'){
mail bcc: '', body: '''Build successful for everyone!!!!
Thanks,
Sagar''', cc: '', from: '', replyTo: '', subject: 'Build successfull', to: 'vs.sagar@gmail.com'
}}

