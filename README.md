# DEVOPS-TASK-
```
job("github_pull")
{
  scm{
    
    github("vishnupal/DEVOPS-TASK-6")
    
  }
  
  triggers{
        
       authenticationToken('git_commit')
    
        githubPush()
  
}
  
  steps{
    
      shell("sudo cp -rvf * /storage")   
    if(shell("sudo ls /storage/ | grep html ")) {
      dockerBuilderPublisher {
            dockerFileDirectory("/storage/")            
            cloud("docker")
        tagsString("9057508163/html:v1")
            pushOnSuccess(true)
      
            fromRegistry {
                  url("9057508163")
                  credentialsId("4d43a672-9085-4ce0-964a-666f02662504")
            }
            pushCredentialsId("4d43a672-9085-4ce0-964a-666f02662504")
            cleanImages(false)

            cleanupWithJenkinsJobDelete(false)
            noCache(false)
            pull(true)
           
      }
}else {
      dockerBuilderPublisher {
            dockerFileDirectory("/storage/")            
        cloud("docker")
        tagsString("9057508163/php:v1")
            pushOnSuccess(true)
      
            fromRegistry {
                  url("9057508163")
                  credentialsId("4d43a672-9085-4ce0-964a-666f02662504")
            }
            pushCredentialsId("4d43a672-9085-4ce0-964a-666f02662504")
                cleanImages(false)

            cleanupWithJenkinsJobDelete(false)
            noCache(false)
            pull(true)
}
 }
}
}
job("detect_DSL"){
  
   triggers {
        upstream('github_pull', 'SUCCESS')
    }
  
  steps{
    
    shell("if sudo ls /storage/ | grep html; then sudo curl -u admin:redhat http://192.168.43.151:8080/job/html_dep_DSL/build?token=html_dep; else   if sudo ls /storage/ | grep php;  then sudo  curl -u admin:redhat http://192.168.43.151:8080/job/php_dep_DSL/build?token=php_dep;fi;fi;if sudo ls /storage/ | grep php;then sudo curl -u admin:redhat http://192.168.43.151:8080/job/php_dep/build?token=php_success;fi;")
}
}

job("html_dep_DSL")
{
  
  triggers{
    authenticationToken('html_dep')
    upstream('detect_DSL','SUCCESS')
    
  }
  
  steps{
    shell("if sudo kubectl get pvc | grep html;then if sudo  kubectl get deploy | grep html; then  sudo kubectl set image deploy/html-app html-con=9057508163/html:v1;  else sudo kubectl create -f /storage/create_html_deploy.yml;fi;else sudo kubectl create -f /storage/create_html_deploy.yml;fi;")
  }
}



job("php_dep_DSL")
{
  
  triggers{
    authenticationToken('php_dep')
   
    upstream('detect_DSL','SUCCESS')
    
  }
  
  steps{
    shell("if sudo kubectl get pvc | grep php;then if sudo kubectl get deploy | grep php; then  sudo  kubectl set image deploy/html-app html-con=90575081630/php:v1;  else sudo kubectl create -f /storage/create_html_deploy.yml;fi;else sudo kubectl create -f /storage/create_php_deploy.yml;fi;")
  }
}

job("test_DSL") {
   triggers{
    
    upstream("php_dep_DSL,html_dep_DSL")
   }
steps {
    
    shell('export status=$(curl -siw "%{http_code}" -o /dev/null 192.168.43.151:32000); if [ $status -eq 200 ]; then exit 0; else python3 /storage/mail.py; exit 1; fi')  }
}
```
