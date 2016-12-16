node('slave') {
    step([$class: 'WsCleanup'])
    stage('check-out-code') {
        checkout scm
    }
    stash 'build'
}


if (env.BRANCH_NAME == 'master') {
    def version = new Date().format("yyyy-MM-dd-'T'HH-mm-ss")
    withEnv([
        "DOCKER_REVISION=${version}",
    ]) {
        node('slave') {
            step([$class: 'WsCleanup'])
            unstash 'build'

            stage('cook-prod-image') {
                sh 'make cook-image'
            }

            stash 'build'
        }

        node('deploy') {
            step([$class: 'WsCleanup'])
            unstash 'build'

            stage('push-to-registry') {
                sh 'make push-image'
            }

            stage('deploy-to-prod') {
                build job: 'marathon-deploy-app', parameters: [
                    [$class: 'StringParameterValue', name: 'app', value: 'pma'],
                    [$class: 'StringParameterValue', name: 'version', value: version],
                ]
            }
        }
    }
} else {
    node('slave') {
        step([$class: 'WsCleanup'])
        unstash 'build'
        stage('test-cook-image') {
            sh 'make cook-image'
        }
    }
}


// vim: ft=groovy
