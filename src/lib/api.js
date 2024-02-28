// const axios = require('axios');

// const config = {
// 	apiBasePath: 'http://localhost:8000',
// 	reactAppMode: 'dev',
//   };

// class APIClient {
//   constructor(overrides) {
// 	this.config = {
// 	  ...config,
// 	  ...overrides,
// 	};
// 	this.authToken = config.authToken;

// 	this.login = this.login.bind(this);
// 	this.apiClient = this.getApiClient(this.config);
//   }

//   /* ----- Authentication & User Operations ----- */

//   /* Authenticate the user with the backend services.
// 	 * The same JWT should be valid for both the api and cms */
//   login(username, password) {
// 	delete this.apiClient.defaults.headers['Authorization'];

// 	// HACK: This is a hack for scenario where there is no login form
// 	const form_data = new FormData();
// 	const grant_type = 'password';
// 	const item = {grant_type, username, password};
// 	for (const key in item) {
// 	  form_data.append(key, item[key]);
// 	}

// 	return this.apiClient
// 		.post('/auth/login', form_data)
// 		.then((resp) => {
// 		  return this.fetchUser();
// 		});
//   }

//   fetchUser() {
// 	return this.apiClient.get('/auth/me').then(({data}) => {
// 	  return data;
// 	});
//   }

//   register(email, password, fullName) {
// 	const registerData = {
// 	  email,
// 	  password,
// 	  full_name: fullName,
// 	  is_active: true,
// 	};

// 	return this.apiClient.post('/auth/signup', registerData).then(
// 		(resp) => {
// 		  return resp.data;
// 		});
//   }

//   // Logging out is just deleting the jwt.
//   logout() {
// 	// Add here any other data that needs to be deleted from local storage
// 	// on logout
//   }

//   /* ----- Client Configuration ----- */

//   /* Create Axios client instance pointing at the REST api backend */
// //   getApiClient(config) {
// // 	const initialConfig = {
// // 	  baseURL: `${config.apiBasePath}/api/v1`,
// // 	};
// // 	const client = axios.create(initialConfig);
// // 	client.interceptors.request.use(localStorageTokenInterceptor);
// // 	return client;
// //   }

//   getImageID(id){
// 	return `${config.apiBasePath}/image/id/${id}`
//   }

//   getImageName(name){
// 	return `${config.apiBasePath}/image/get/${name}`
//   }

//   // <img src="">

// //   getRecipe(recipeId) {
// //     return this.apiClient.get(`/recipes/${recipeId}`);
// //   }

// //   getRecipes(keyword) {
// //     return this.apiClient.get(`/recipes/search/?keyword=${keyword}&max_results=10`).then(({data}) => {
// //       return data;
// //     });
// //   }

// //   getUserRecipes() {
// //     return this.apiClient.get(`/recipes/my-recipes/`).then(({data}) => {
// //       return data;
// //     });
// //   }

// //   createRecipe(label, url, source, submitter_id) {
// //     const recipeData = {
// //       label,
// //       url,
// //       source,
// //       submitter_id: submitter_id,
// //     };
// //     return this.apiClient.post(`/recipes/`, recipeData);
// //   }


// //   deleteRecipe(recipeId) {
// //     return this.apiClient.delete(`/recipes/${recipeId}`);
// //   }
// }

// export default APIClient;