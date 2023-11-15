// pipeline {
//     agent {
//         docker {
//             image 'node:20.9.0-alpine3.18'
//             args '-p 3000:3000'
//         }
//     }
//     stages {
//         stage('Build') {
//             steps {
//                 sh 'npm install'
//             }
//         }
//         stage('Test') {
//             steps {
//                 sh './jenkins/scripts/test.sh'
//             }
//         }
//         stage('Deliver') { 
//             steps {
//                 sh './jenkins/scripts/deliver.sh' 
//                 input message: 'Finished using the web site? (Click "Proceed" to continue)' 
//                 sh './jenkins/scripts/kill.sh' 
//             }
//         }
//         stage('OWASP Dependency-Check Vulnerabilities') {
//             steps {
//                 dependencyCheck additionalArguments: ''' 
//                             -o './'
//                             -s './'
//                             -f 'ALL' 
//                             --prettyPrint''', odcInstallation: 'OWASP Dependency-Check Vulnerabilities'
                
//                 dependencyCheckPublisher pattern: 'dependency-check-report.xml'
//             }
//         }

//         stage('Code Quality Check via SonarQube') {
//             steps {
//                 script {
//                     def scannerHome = tool 'SonarQube'
//                     withSonarQubeEnv('SonarQube') {
//                         sh "${scannerHome}/bin/sonar-scanner \
//                             -Dsonar.projectKey=OWASP \
//                             -Dsonar.sources=. \
//                             -Dsonar.host.url=http://127.0.0.1:9000 \
//                             -Dsonar.token=sqp_af4c3c6c3b4addbda6f1ba03affa2a1b13ebaadc"
//                     }
//                 }
//             }
//         }

//         stage('Integration UI Test') {
// 			parallel {
// 				stage('Deploy') {
// 					agent any
// 					steps {
// 						sh 'chmod +x jenkins/scripts/deploy.sh'
// 						sh 'chmod +x jenkins/scripts/kill.sh'

// 						sh './jenkins/scripts/deploy.sh'
// 						input message: 'Finished using the web site? (Click "Proceed" to continue)'
// 						sh './jenkins/scripts/kill.sh'
// 					}
// 				}
// 				stage('Headless Browser Test') {
// 					agent {
// 						docker {
// 							image 'maven:3-alpine' 
// 							args '-v /root/.m2:/root/.m2' 
// 						}
// 					}
// 					steps {
// 						sh 'mvn -B -DskipTests clean package'
// 						sh 'mvn test'
// 					}
// 					post {
// 						always {
// 							junit 'target/surefire-reports/*.xml'
// 						}
// 					}
// 				}
// 			}
// 		}
//     }
// }


pipeline {
	agent any
	stages {
		stage('Checkout SCM') {
			steps {
				git 'https://github.com/banananiee/JenkinsDependencyCheckTest.git'
			}
		}

		stage('OWASP Dependency-Check Vulnerabilities') {
			steps {
				dependencyCheck additionalArguments: '--format HTML --format XML --suppression suppression.xml', odcInstallation: 'OWASP Dependency-Check Vulnerabilities'
			}
		}
	}	
	post {
		success {
			dependencyCheckPublisher pattern: 'dependency-check-report.xml'
		}
	}
}