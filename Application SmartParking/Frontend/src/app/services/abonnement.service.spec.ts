import { TestBed } from '@angular/core/testing';

import { AbonnementService } from './abonnement.service';

describe('AbonnementService', () => {
  let service: AbonnementService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(AbonnementService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
