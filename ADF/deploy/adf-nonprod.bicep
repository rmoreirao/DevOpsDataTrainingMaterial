param dataFactoryName string
param location string
param repositoryType string = 'FactoryVSTSConfiguration'
param projectName string  = 'Module 6'
param repositoryName string = 'Module 6'
param accountName string = 'dataprimetraining'
param collaborationBranch string = 'master'
param rootFolder string = '/ADF/src'

resource dataFactory 'Microsoft.DataFactory/factories@2018-06-01' = {
  name: dataFactoryName
  location: location
  identity: {
    type: 'SystemAssigned'
  }
  properties: {
    repoConfiguration: {
      accountName: accountName
      repositoryName: repositoryName
      collaborationBranch: collaborationBranch
      rootFolder: rootFolder  
      type: repositoryType
      projectName: projectName
    }
  }

}

output dataFactoryId string = dataFactory.id
