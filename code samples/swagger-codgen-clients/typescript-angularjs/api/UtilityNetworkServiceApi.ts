/**
 * Swagger for Utility Network
 * Open API Specification (OAS/Swagger)  * **trace**, **updateIsConnected** from the [ArcGIS Utility Network]( https://developers.arcgis.com/rest/services-reference/utility-network-service.htm) * **generateToken** from the [ArcGIS REST API](https://developers.arcgis.com/rest/)  Tested on ArcGIS  Enterprise 10.6.1 using [NSwagStudio](https://github.com/RSuter/NSwag/wiki/NSwagStudio) C# code gen . 
 *
 * OpenAPI spec version: 0.13
 * Contact: 
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 */

import * as models from '../model/models';

/* tslint:disable:no-unused-variable member-ordering */

export class UtilityNetworkServiceApi {
    protected basePath = 'https://t4e7j4g.restletmocks.net';
    public defaultHeaders : any = {};

    static $inject: string[] = ['$http', '$httpParamSerializer', 'basePath'];

    constructor(protected $http: ng.IHttpService, protected $httpParamSerializer?: (d: any) => any, basePath?: string) {
        if (basePath !== undefined) {
            this.basePath = basePath;
        }
    }

    /**
     * 
     * @summary generateToken
     * @param portalWebAdaptor 
     * @param username 
     * @param password 
     * @param expiration 
     * @param f 
     * @param ip 
     * @param referer 
     */
    public portalWebAdaptorSharingRestGenerateTokenPost (portalWebAdaptor: string, username: string, password: string, expiration: number, f: string, ip?: string, referer?: string, extraHttpRequestParams?: any ) : ng.IHttpPromise<models.TokenResponse> {
        const localVarPath = this.basePath + '/{PortalWebAdaptor}/sharing/rest/generateToken'
            .replace('{' + 'PortalWebAdaptor' + '}', encodeURIComponent(String(portalWebAdaptor)));

        let queryParameters: any = {};
        let headerParams: any = (<any>Object).assign({}, this.defaultHeaders);
        let formParams: any = {};

        // verify required parameter 'portalWebAdaptor' is not null or undefined
        if (portalWebAdaptor === null || portalWebAdaptor === undefined) {
            throw new Error('Required parameter portalWebAdaptor was null or undefined when calling portalWebAdaptorSharingRestGenerateTokenPost.');
        }

        // verify required parameter 'username' is not null or undefined
        if (username === null || username === undefined) {
            throw new Error('Required parameter username was null or undefined when calling portalWebAdaptorSharingRestGenerateTokenPost.');
        }

        // verify required parameter 'password' is not null or undefined
        if (password === null || password === undefined) {
            throw new Error('Required parameter password was null or undefined when calling portalWebAdaptorSharingRestGenerateTokenPost.');
        }

        // verify required parameter 'expiration' is not null or undefined
        if (expiration === null || expiration === undefined) {
            throw new Error('Required parameter expiration was null or undefined when calling portalWebAdaptorSharingRestGenerateTokenPost.');
        }

        // verify required parameter 'f' is not null or undefined
        if (f === null || f === undefined) {
            throw new Error('Required parameter f was null or undefined when calling portalWebAdaptorSharingRestGenerateTokenPost.');
        }

        headerParams['Content-Type'] = 'application/x-www-form-urlencoded';

        formParams['username'] = username;

        formParams['password'] = password;

        formParams['ip'] = ip;

        formParams['referer'] = referer;

        formParams['expiration'] = expiration;

        formParams['f'] = f;

        let httpRequestParams: ng.IRequestConfig = {
            method: 'POST',
            url: localVarPath,
            data: this.$httpParamSerializer(formParams),
            params: queryParameters,
            headers: headerParams
        };

        if (extraHttpRequestParams) {
            httpRequestParams = (<any>Object).assign(httpRequestParams, extraHttpRequestParams);
        }

        return this.$http(httpRequestParams);
    }
    /**
     * Trace
     * @summary trace
     * @param serverWebAdaptor 
     * @param utilityNetworkName 
     * @param token 
     * @param f Optional parameter representing the output format of the response (default is JSON).
     * @param traceType The trace type.
     * @param traceLocations ***Curently a workaround until figure out how to gen**The locations for starting and stopping points, as well as barriers. Optional parameter for subnetwork trace type, required parameter for all other trace types.
     * @param traceConfiguration The locations for starting and stopping points, as well as barriers. Optional parameter for subnetwork trace type, required parameter for all other trace types.
     * @param gdbVersion The name of the geodatabase version.
     * @param sessionId Optional parameter representing the token (guid) used to lock the version. If the calling client has previously started a service session (editing) and holds an exclusive lock on the specified version, the request will fail if the sessionId is not provided. If the specified version is currently locked by any other session, the request will fail if the sessionId is not provided or does not match the sessionId which holds the exclusive lock.
     * @param moment Optional parameter representing the session moment (the default is the version current moment). This should only be specified by the client when they do not want to use the current moment.
     */
    public trace (serverWebAdaptor: string, utilityNetworkName: string, token: string, f: string, traceType: models.'upstream' | 'downstream' | 'connected' | 'subnetwork' | 'unknown' | 'loops' | 'shortestpath' | 'subnetworkcontroller', traceLocations: string, traceConfiguration: string, gdbVersion?: string, sessionId?: string, moment?: string, extraHttpRequestParams?: any ) : ng.IHttpPromise<models.TraceResultsSet> {
        const localVarPath = this.basePath + '/{ServerWebAdaptor}/rest/services/{UtilityNetworkName}/UtilityNetworkServer/trace'
            .replace('{' + 'ServerWebAdaptor' + '}', encodeURIComponent(String(serverWebAdaptor)))
            .replace('{' + 'UtilityNetworkName' + '}', encodeURIComponent(String(utilityNetworkName)));

        let queryParameters: any = {};
        let headerParams: any = (<any>Object).assign({}, this.defaultHeaders);
        let formParams: any = {};

        // verify required parameter 'serverWebAdaptor' is not null or undefined
        if (serverWebAdaptor === null || serverWebAdaptor === undefined) {
            throw new Error('Required parameter serverWebAdaptor was null or undefined when calling trace.');
        }

        // verify required parameter 'utilityNetworkName' is not null or undefined
        if (utilityNetworkName === null || utilityNetworkName === undefined) {
            throw new Error('Required parameter utilityNetworkName was null or undefined when calling trace.');
        }

        // verify required parameter 'token' is not null or undefined
        if (token === null || token === undefined) {
            throw new Error('Required parameter token was null or undefined when calling trace.');
        }

        // verify required parameter 'f' is not null or undefined
        if (f === null || f === undefined) {
            throw new Error('Required parameter f was null or undefined when calling trace.');
        }

        // verify required parameter 'traceType' is not null or undefined
        if (traceType === null || traceType === undefined) {
            throw new Error('Required parameter traceType was null or undefined when calling trace.');
        }

        // verify required parameter 'traceLocations' is not null or undefined
        if (traceLocations === null || traceLocations === undefined) {
            throw new Error('Required parameter traceLocations was null or undefined when calling trace.');
        }

        // verify required parameter 'traceConfiguration' is not null or undefined
        if (traceConfiguration === null || traceConfiguration === undefined) {
            throw new Error('Required parameter traceConfiguration was null or undefined when calling trace.');
        }

        if (token !== undefined) {
            queryParameters['token'] = token;
        }

        headerParams['Content-Type'] = 'application/x-www-form-urlencoded';

        formParams['f'] = f;

        formParams['gdbVersion'] = gdbVersion;

        formParams['sessionId'] = sessionId;

        formParams['moment'] = moment;

        formParams['traceType'] = traceType;

        formParams['traceLocations'] = traceLocations;

        formParams['traceConfiguration'] = traceConfiguration;

        let httpRequestParams: ng.IRequestConfig = {
            method: 'POST',
            url: localVarPath,
            data: this.$httpParamSerializer(formParams),
            params: queryParameters,
            headers: headerParams
        };

        if (extraHttpRequestParams) {
            httpRequestParams = (<any>Object).assign(httpRequestParams, extraHttpRequestParams);
        }

        return this.$http(httpRequestParams);
    }
}
