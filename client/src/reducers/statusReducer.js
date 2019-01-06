import { UPDATE_STATUS } from '../actions/actionTypes';

export default (state = 'Initializing...', action) => {
  switch (action.type) {
    case UPDATE_STATUS:
      return action.payload;
    default:
      return state;
  }
};
